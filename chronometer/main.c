#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int compare(const void *a, const void *b) {
    double diff = (*(double*)a - *(double*)b);
    return (diff > 0) - (diff < 0);
}

double percentile(double *arr, int n, double p) {
    double idx = p * (n - 1);
    int i = (int)idx;
    double frac = idx - i;

    if (i + 1 < n)
        return arr[i] * (1 - frac) + arr[i + 1] * frac;
    else
        return arr[i];
}

int main() {
    int N = 10000;
    double times[N];

    struct timespec start, end;
    FILE *fp;

    for (int i = 0; i < N; i++) {

        clock_gettime(CLOCK_MONOTONIC, &start);

        fp = popen("./generation", "r");

        if (!fp) {
            printf("Erreur lors de l'exécution du script Python.\n");
            return 1;
        }


        char buffer[64];
        fgets(buffer, sizeof(buffer), fp);

        pclose(fp);

        clock_gettime(CLOCK_MONOTONIC, &end);

        double elapsed_ms =
            (end.tv_sec - start.tv_sec) * 1000.0 +
            (end.tv_nsec - start.tv_nsec) / 1e6;

        times[i] = elapsed_ms;
    }

    // Tri des temps
    qsort(times, N, sizeof(double), compare);

    // Statistiques
    double min = times[0];
    double max = times[N - 1];
    double q1 = percentile(times, N, 0.25);
    double q2 = percentile(times, N, 0.50); // médiane
    double q3 = percentile(times, N, 0.75);
    double wcet = max * 1.1;

    printf("\n===== STATISTIQUES D'EXECUTION =====\n");
    printf("Min   : %.3f ms\n", min);
    printf("Q1    : %.3f ms\n", q1);
    printf("Q2    : %.3f ms (médiane)\n", q2);
    printf("Q3    : %.3f ms\n", q3);
    printf("Max   : %.3f ms\n", max);
    printf("WCET=max*1.1  : %.3f ms\n", wcet);

    return 0;
}
