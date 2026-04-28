#include <iostream>
#include <random>
#include <cstdint>

using namespace std;

static std::mt19937_64 gen(std::random_device{}());

__int128 random_big() {
    std::uniform_int_distribution<uint64_t> dist(0, UINT64_MAX);
    __int128 high = (__int128)dist(gen);
    __int128 low  = (__int128)dist(gen);
    return (high << 64) | low;   // nombre 128 bits
}

__int128 generation_number() {
    __int128 x = random_big();
    __int128 y = random_big();
    return x * y;
}

void print128(__int128 v) {
    if (v < 0) { cout << "-"; v = -v; }
    if (v > 9) print128(v / 10);
    cout << (int)(v % 10);
}

int main() {
    __int128 result = generation_number();
    print128(result);
    return 0;
}
