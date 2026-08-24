// 15_digital_clock.c — the final project: a working digital clock
// Windows:  gcc 15_digital_clock.c -o clock   then   clock.exe
// Linux:    gcc 15_digital_clock.c -o clock   then   ./clock
#include <stdio.h>
#include <time.h>

#ifdef _WIN32
  #include <windows.h>     // provides Sleep(1000) — milliseconds
#else
  #include <unistd.h>      // provides sleep(1) — seconds
#endif

int main() {
    time_t rawTime;              // seconds since the "epoch" (Jan 1, 1970)
    struct tm *pTime;            // readable breakdown: hours, minutes, seconds
    int isRunning = 1;

    while (isRunning) {
        rawTime = time(NULL);            // update the raw seconds
        pTime = localtime(&rawTime);     // convert to a time struct

        // %02d = zero-pad to 2 digits; \r = carriage return (update in place)
        printf("%02d:%02d:%02d\r",
               pTime->tm_hour, pTime->tm_min, pTime->tm_sec);
        fflush(stdout);                  // force the output to appear

#ifdef _WIN32
        Sleep(1000);                     // 1000 MILLIseconds on Windows
#else
        sleep(1);                        // 1 SECOND on Linux/Mac
#endif
    }
    return 0;
}