import type { Plugin } from "@opencode-ai/plugin"
import { readFile, stat } from "node:fs/promises"
import { join } from "node:path"

const SIZE_LIMIT = 25_000
const EXEMPT = [".obsidian", ".opencode", "node_modules", "templates", "raw-sources"]

function normalize(p: string): string {
  return p.replaceAll("\\", "/")
}

function isExempt(rel: string): boolean {
  const parts = rel.split("/")
  return EXEMPT.some((e) => parts.includes(e))
}

export const MindPlugin: Plugin = async ({ directory }) => {
  return {
    "tool.execute.after": async (input, output) => {
      try {
        if (!["write", "edit"].includes(input.tool)) return
        const rawPath = String(output.args?.filePath ?? output.args?.file_path ?? "")
        if (!rawPath || !rawPath.endsWith(".md")) return
        const abs = rawPath.startsWith(directory) ? rawPath : join(directory, rawPath)
        const rel = normalize(abs.slice(directory.length)).replace(/^\//, "")
        if (isExempt(rel)) return

        const [text, s] = await Promise.all([readFile(abs, "utf8"), stat(abs)])
        const hints: string[] = []

        const fm = text.match(/^---\r?\n([\s\S]*?)\r?\n---/)
        if (!fm) {
          hints.push("no YAML frontmatter — add date, description (~150 chars), tags")
        } else {
          for (const key of ["date", "description", "tags"]) {
            if (!new RegExp(`^${key}:`, "m").test(fm[1]))
              hints.push(`frontmatter missing \`${key}\``)
          }
        }

        const links = (text.match(/\[\[[^\]]+\]\]/g) ?? []).length
        if (links === 0 && !rel.startsWith("daily/") && !rel.startsWith("thinking/"))
          hints.push("zero wikilinks — a note without links is a bug")

        if (s.size > SIZE_LIMIT)
          hints.push(
            `${(s.size / 1024).toFixed(0)}KB exceeds the ~25KB structure signal — split into atomic linked notes instead of growing further`
          )

        if (hints.length > 0)
          output.result =
            (output.result ?? "") + `\n\n[mind] ${hints.join("; ")}`
      } catch {
        // validation must never break a write
      }
    },

    "experimental.session.compacting": async (_input, output) => {
      output.context.push(
        [
          "## Vault persistence rules",
          `- Durable knowledge belongs in vault files before this summary matters: decisions -> brain/Key Decisions.md, gotchas -> brain/Gotchas.md, patterns -> brain/Patterns.md, wins -> brain/Wins.md`,
          "- Route study material via wiki/modules/<subject>/ with full frontmatter; update wiki/index.md and wiki/log.md",
          "- Current goals live in brain/North Star.md — preserve any goal shifts in the summary",
          "- Every note needs frontmatter and at least one [[wikilink]]; say 'wrap up' triggers /om-wrap-up",
        ].join("\n")
      )
    },
  }
}
