"""Love-note round verification: user's exact test string + prose paragraph + gates."""
import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import inference as inf

style = json.load(open('styles/user_001.style'))
note = (
    "Kedar I love you soo so much yr, i just wanna come and hug you tight, "
    "im soo so in love with you!!!"
)
img = inf.render_labeled(note, style, 'styles/user_001.labeled', seed=7)
img.save('outputs/Proof-lovenote-seed7.png')
print('lovenote', img.size)
para = (
    "Your text was completely fine—it was grammatically clear, natural, and friendly, "
    "but because it didn't name the specific company, college committee, or program, "
    "I couldn't look up an exact date for you. The reason you got a follow-up question "
    "instead of a direct answer is simply that interview result timelines vary wildly "
    "depending on the organization. If you add the name of the place you interviewed "
    "with, I'd be happy to check if there is an official announcement schedule or "
    "share their typical response timeframe!"
)
img = inf.render_labeled(para, style, 'styles/user_001.labeled', seed=7)
img.save('outputs/Proof-prose-seed7.png')
print('prose', img.size)
for seed in (7, 11, 23, 42):
    w = inf.render_labeled(
        'were you u it in have to check', style, 'styles/user_001.labeled', seed=seed)
    w.save(f'outputs/Proof-gate-seed{seed}.png')
    print('gate', seed, w.size)
