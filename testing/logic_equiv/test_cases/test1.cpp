// expected to replace: 702
#include "stdio.h"
#include "time.h"
#include "stdlib.h"
#include <iostream>
#include <chrono>
using namespace std;

// From https://stackoverflow.com/questions/33058848/generate-a-random-double-between-1-and-1
/* generate a random floating point number from min to max */
double randfrom(double min, double max) 
{
    double range = (max - min); 
    double div = RAND_MAX / range;
    return min + (rand() / div);
}

double op_function(double a, double b, double c, double d, double e, double f, double g, double h, double i, double j, double k, double l, double m, double n, double o, double p, double q, double r) {
  // Start optimization range
    d = l - k;
    b = p - k;
    d = r - n;
    e = o + j;
    g = r + m;
    b = q - o;
    e = o - j;
    e = m - p;
    i = k - q;
    b = n + m;
    b = l - j;
    i = n - q;
    c = k - k;
    c = l + n;
    b = q - o;
    h = o - j;
    c = r + q;
    i = q + n;
    c = q - l;
    e = j - l;
    c = q + j;
    h = n - o;
    d = p - p;
    h = q + q;
    c = k + n;
    d = l + q;
    f = j + n;
    i = m - k;
    e = o + o;
    h = j + l;
    b = m + r;
    h = o + r;
    g = o + m;
    b = q + n;
    h = o - m;
    b = p + r;
    a = n - o;
    h = q + n;
    f = n + m;
    c = q + k;
    f = q - k;
    a = k - n;
    g = r + q;
    g = q + n;
    i = k - q;
    f = j + j;
    d = n + m;
    e = k - j;
    c = k + l;
    e = m + q;
    b = m - m;
    c = o + r;
    d = m + j;
    q = j + r;
    d = o - n;
    c = k + j;
    i = l + k;
    f = q + q;
    h = n - l;
    h = n - n;
    a = l + k;
    c = r - j;
    h = j - p;
    e = k - k;
    h = k + q;
    e = r - q;
    b = p + r;
    i = r + l;
    h = p + m;
    i = n + m;
    f = o + p;
    d = j - l;
    e = k + q;
    f = o - k;
    d = p - n;
    f = o - k;
    b = o - j;
    e = m - j;
    i = q - p;
    f = n + p;
    i = o + r;
    b = r + k;
    a = n - o;
    h = j - j;
    b = p - n;
    e = j - l;
    e = r - o;
    f = p - o;
    i = n + n;
    g = l + q;
    b = q + o;
    g = k + m;
    b = k + n;
    c = l - p;
    i = o + k;
    a = l + l;
    h = l + q;
    c = r + o;
    b = l - n;
    c = p - m;
    d = n - p;
    a = n - q;
    o = l + n;
    e = p + l;
    h = j - j;
    i = r - n;
    h = q + o;
    b = k + m;
    f = l + n;
    e = k + k;
    p = q - j;
    d = m - k;
    h = r - f;
    h = j - l;
    b = p - r;
    c = k + q;
    e = q - m;
    i = n + o;
    h = r + l;
    e = k - n;
    g = p + o;
    h = j + m;
    d = n + p;
    i = k - p;
    f = l - o;
    g = p - r;
    b = p - p;
    i = n + p;
    g = n - o;
    c = k + o;
    e = m + k;
    i = o - k;
    b = k + m;
    d = q - p;
    i = q + m;
    g = q - j;
    b = o - m;
    f = k - r;
    a = m + k;
    i = m - p;
    d = o + m;
    f = l + o;
    i = l - m;
    a = m - l;
    e = o + n;
    k = n - l;
    i = k + p;
    d = r - k;
    a = r - p;
    g = l + j;
    e = l - q;
    d = n - k;
    e = o - n;
    a = o - j;
    g = n - l;
    e = l + l;
    a = l + r;
    a = j + j;
    a = k - m;
    i = k + r;
    f = k + m;
    a = o - p;
    e = o + p;
    i = l + k;
    c = q - n;
    a = k + l;
    a = r - k;
    d = j - j;
    b = p - m;
    g = m - m;
    c = j - l;
    d = m - m;
    a = m - k;
    e = m - n;
    d = k + i;
    i = o + j;
    a = o - l;
    f = q + m;
    e = l + m;
    g = m - q;
    f = p + o;
    f = p - o;
    f = l + k;
    b = r + l;
    d = r + k;
    e = o - m;
    h = p - n;
    a = l + o;
    h = r + q;
    i = r + j;
    f = l + k;
    h = k + n;
    d = p - p;
    f = p + p;
    d = q - n;
    b = p - r;
    e = o - l;
    a = m + j;
    e = j - n;
    e = r + l;
    f = r - o;
    g = l - r;
    b = m + p;
    d = q + k;
    b = q - n;
    c = o - j;
    g = n + n;
    h = k + m;
    i = n - j;
    d = j - m;
    i = p - l;
    f = p - k;
    b = l + m;
    h = l + k;
    e = m - k;
    i = o - q;
    a = n - l;
    f = j + l;
    b = d + m;
    b = m - r;
    a = o + l;
    i = m + l;
    a = p + l;
    f = o - k;
    a = r + q;
    e = j + o;
    e = n + j;
    g = l + l;
    l = o + q;
    e = m - p;
    c = r + o;
    a = o - n;
    b = q + n;
    g = r + j;
    d = r - l;
    h = p + r;
    i = r - o;
    b = j - o;
    f = o - m;
    c = j - n;
    f = m - o;
    b = m - l;
    g = j - l;
    e = o + m;
    g = q + l;
    i = l - j;
    b = q + j;
    f = o + p;
    d = r + p;
    c = l + l;
    d = m + l;
    a = q + q;
    d = p + p;
    e = p + m;
    d = k + l;
    b = l - p;
    h = m - o;
    e = k - q;
    b = k - r;
    f = q - j;
    e = q - l;
    i = n - m;
    g = o + m;
    f = r + n;
    e = j + j;
    d = p + m;
    h = k + l;
    e = o + m;
    a = o - j;
    c = l - a;
    d = m + j;
    f = p - m;
    c = n - m;
    d = j - j;
    i = o + j;
    b = n - p;
    i = p - q;
    d = k - o;
    a = q + r;
    c = o + k;
    i = q + p;
    d = p + n;
    g = r + k;
    b = k + m;
    b = p + r;
    h = n - q;
    d = o + k;
    b = q + r;
    i = r - p;
    f = r - l;
    f = r - r;
    h = k - p;
    i = p - l;
    a = j - k;
    f = n + j;
    d = o - p;
    g = j - j;
    i = o + o;
    f = m - o;
    f = m - b;
    i = o - n;
    b = l + l;
    e = k + l;
    i = n + r;
    f = n - r;
    c = o + p;
    a = q + m;
    b = k + o;
    d = o - l;
    e = q - r;
    g = l + o;
    h = r - r;
    i = j - j;
    f = m + l;
    h = n - o;
    a = j + p;
    f = n - l;
    h = o - p;
    d = l + l;
    d = r - n;
    g = q - k;
    e = l - l;
    b = o - o;
    f = l + l;
    c = q - r;
    d = q - q;
    d = n + j;
    a = j - o;
    g = o - j;
    a = l - p;
    h = q - q;
    e = r - m;
    g = k + p;
    c = o - p;
    g = q + l;
    e = r - k;
    b = r + k;
    b = l - r;
    c = m - q;
    e = o - j;
    b = l - j;
    f = r + n;
    i = q - k;
    b = k + j;
    h = r + r;
    f = q + m;
    g = r - n;
    f = r + j;
    c = l + l;
    d = m - r;
    i = n + q;
    c = l - j;
    c = o + l;
    h = o - n;
    h = n + n;
    c = m - l;
    c = j - n;
    g = k + n;
    c = o + q;
    b = k - n;
    c = r - l;
    h = r + p;
    a = m + q;
    e = k - r;
    g = l + j;
    e = r - k;
    i = q + l;
    h = r - q;
    i = o + k;
    i = n + n;
    g = l + q;
    f = j + n;
    d = k + o;
    g = q - q;
    d = j - p;
    i = j - l;
    f = n + k;
    f = n - j;
    b = r + o;
    d = q + o;
    b = m - j;
    a = k - r;
    h = j - m;
    d = j + j;
    c = l + j;
    c = n - q;
    i = q - q;
    g = j - j;
    e = k + l;
    b = r + p;
    g = n - q;
    i = o + l;
    h = k - k;
    b = q + p;
    d = o - j;
    c = n - k;
    g = j - m;
    i = r + l;
    i = k + m;
    h = k + q;
    g = o + o;
    i = k + o;
    d = k + j;
    c = j + m;
    i = p - m;
    h = d + l;
    f = o - m;
    b = k + n;
    c = p - m;
    a = r - q;
    f = p + c;
    i = r + m;
    i = k + n;
    e = m + p;
    a = j + l;
    d = m + k;
    d = m - p;
    h = l + q;
    b = k - p;
    i = n + m;
    h = p - o;
    e = r - j;
    b = r + o;
    d = m - p;
    c = r - j;
    h = k + k;
    b = j - q;
    h = r + m;
    f = n - p;
    b = q + p;
    c = m + l;
    i = m - o;
    d = m - p;
    c = m + l;
    b = q - o;
    e = m - j;
    d = n + p;
    a = p - q;
    f = q - k;
    i = n - j;
    g = q + k;
    c = l - o;
    c = r + m;
    d = r + o;
    h = r - p;
    b = l - j;
    d = o + q;
    e = q + l;
    c = o - o;
    e = r - o;
    c = q + o;
    e = k + n;
    h = m - k;
    e = r + r;
    c = k - n;
    a = r + o;
    b = r - l;
    d = m + k;
    d = o - q;
    d = i - l;
    g = p - n;
    i = l + o;
    e = m - k;
    a = l + j;
    i = k - p;
    i = m - j;
    a = o + m;
    i = p + p;
    b = q - p;
    a = l - o;
    h = o - j;
    b = k + r;
    f = l - m;
    b = n - o;
    f = k - k;
    a = p - m;
    h = k + j;
    f = m - o;
    a = q - q;
    h = k - j;
    g = k - r;
    e = r + m;
    i = l - r;
    i = l + m;
    a = r + p;
    c = k + n;
    c = n + j;
    a = j + n;
    g = r + l;
    e = l + l;
    c = m + l;
    f = o + q;
    f = q - m;
    b = n + j;
    b = n + l;
    d = m - l;
    g = q + r;
    g = r + m;
    d = n - m;
    e = p - n;
    c = r - l;
    b = j - r;
    f = r + p;
    h = p - p;
    b = n + l;
    h = o + l;
    a = r + j;
    b = j - k;
    b = o - q;
    h = q + p;
    h = k + m;
    d = j - k;
    i = o - q;
    i = o - p;
    h = q - m;
    i = r + r;
    g = n + q;
    h = n + k;
    n = l - q;
    e = j - j;
    c = r - q;
    f = k - p;
    l = n + k;
    c = d + p;
    e = l - m;
    g = r + o;
    a = o + j;
    f = r + k;
    e = m + n;
    i = n - j;
    g = k + r;
    a = l - j;
    c = r - m;
    b = n + m;
    b = j - l;
    g = r + q;
    e = l + r;
    e = n - p;
    d = l + m;
    d = l + p;
    a = p - j;
    f = q + k;
    f = l + r;
    e = o - o;
    b = k + m;
    d = l - o;
    b = k + j;
    a = m + j;
    e = q - n;
    f = r + l;
    h = q - p;
    c = r - p;
    c = n - p;
    h = q + k;
    e = j - k;
    f = m - n;
    a = n - r;
    g = q + o;
    d = l - r;
    a = o - n;
    a = n + q;
    a = j + o;
    d = l + m;
    h = j - q;
    a = n + j;
    b = j - o;
    c = p - j;
    e = r + p;
    a = o - j;
    h = m + r;
    c = q + j;
    f = o - j;
    c = n + p;
    c = k - l;
    i = n - q;
    b = q + p;
    a = p - l;
    d = r + j;
    d = o + p;
    d = o + p;
    d = m + n;
    e = j - m;
    c = m - o;
    e = r + r;
    e = m - m;
    a = l - l;
    c = r - m;
    f = j + k;
    c = j + l;
    e = q + j;
    f = q - q;
    i = q - k;
    c = r + j;
    a = j + q;
    f = m - q;
    g = q + r;
    h = n - j;
    i = o + q;
    h = o - j;
    f = m + j;
    d = k + o;
    h = r - m;
    i = r + j;
    h = m + n;
    d = q + o;
    f = j + n;
    i = r - n;
    i = k + p;
    c = k - p;
    e = n - m;
    b = k - p;
    g = n - j;
    c = p + r;
    c = l + p;
    g = r - n;
    i = n + n;
    c = p + r;
    h = n - j;
    b = q - l;
    a = r - o;
    d = p - l;
    f = j - n;
    e = m - m;
    b = r + r;
    c = o - p;
    a = p + n;
    i = n - r;
    h = l + l;
    e = n - j;
    b = o - j;
    d = r - r;
    a = l + m;
    a = j - p;
    h = p - o;
    b = k - o;
    a = j - o;
    f = r + j;
    g = k - o;
    a = l + k;
    a = l + o;
    l = r - n;
    h = p - l;
    i = k + j;
    c = j - o;
    e = l + n;
    e = l - o;
    g = l - k;
    a = l + p;
    a = q + j;
    h = p - q;
    f = j - r;
    i = n + m;
    c = l + r;
    f = q - o;
    e = r - r;
    g = l + k;
    h = m + q;
    f = q + l;
    h = m + q;
    h = r + p;
    h = o + k;
    a = l - r;
    b = n - m;
    c = o - q;
    e = k + k;
    e = r - l;
    b = n - j;
    d = r + k;
    i = p + m;
    e = p - p;
    a = r + n;
    d = j + n;
    c = o - j;
    h = o + o;
    c = k - o;
    f = r + q;
    g = r + o;
    f = m + p;
    d = l + o;
    b = n + q;
    d = l + j;
    i = m - m;
    b = m - l;
    i = r - l;
    e = p + j;
    c = l - q;
    f = j - p;
    a = j + m;
    h = n + o;
    i = l - k;
    f = p - o;
    c = q + j;
    d = l - m;
    d = m - r;
    d = o + l;
    i = k - o;
    f = m + k;
    d = q + l;
    a = r - r;
    g = p + j;
    i = k - q;
    h = j - o;
    f = l - j;
    e = l + j;
    h = l + j;
    b = q + l;
    e = q - r;
    h = r - q;
    f = l + o;
    f = p + p;
    e = n - k;
    g = k + m;
    i = r + k;
    c = m + r;
    d = m + l;
    a = p + o;
    h = l - p;
    i = n + k;
    e = m - o;
    a = m + m;
    d = k + o;
    f = p + q;
    c = j - k;
    b = n + o;
    b = q + j;
    d = n - j;
    h = j + q;
    h = j + l;
    a = l - m;
    f = r - k;
    g = l - r;
    d = j + o;
    b = j - k;
    b = p + o;
    d = o + r;
    a = r + l;
    d = m - o;
    i = p - o;
    i = o - l;
    b = r + o;
    g = j - n;
    f = m - l;
    b = k + m;
    b = r + l;
    g = m - n;
    h = j - l;
    b = k - n;
    h = p - r;
    i = q - q;
    i = m + q;
    d = o - l;
    e = m + r;
    a = r + p;
    b = o - r;
    c = o - n;
    g = q - j;
    h = o - q;
    i = r + q;
    h = p - p;
    d = l + q;
    d = k - o;
    i = q + l;
    d = p + j;
    d = n + q;
    d = p - m;
    f = l - q;
    f = k + k;
    f = o - m;
    i = k - p;
    a = n - r;
    a = l - o;
    g = q + l;
    e = p - r;
    e = k - q;
    h = r - o;
    b = o - p;
    g = r + q;
    h = m - n;
    c = q + q;
    i = l - r;
    i = m + o;
    h = p + j;
    a = m - r;
    h = n - p;
    i = n + m;
    h = l + r;
    c = o + l;
    a = p - m;
    e = m + q;
    b = p - l;
    g = l - m;
    h = m + n;
    d = p - l;
    h = j + r;
    a = n + o;
    d = n + o;
    b = m + m;
    c = r - l;
    e = q + r;
    b = r - m;
    g = k - l;
    i = o + p;
    i = k + q;
    f = p - q;
    i = o - p;
    c = q - p;
    a = p - r;
    h = p - n;
    c = n + k;
    h = k - n;
    b = n + p;
    d = n - n;
    a = k + q;
    a = n - k;
    i = n + r;
    b = j - r;
    e = q - o;
    d = n - r;
    d = n - p;
    e = m + n;
    b = l - m;
    g = l - n;
    g = j - m;
    b = n + q;
    d = l + k;
    i = p - j;
    b = p - o;
    i = p + d;
    c = k - r;
    e = r - k;
    d = l + l;
    b = m - l;
    d = j - j;
    a = p + j;
    a = k + l;
    g = r - p;
    h = l + k;
    b = j - o;
    b = m + j;
    g = k - p;
    b = o + l;
    i = l + j;
    g = r + j;
    i = r + k;
    c = j - r;
    i = p + r;
    e = n + p;
    d = q + m;
    f = q + p;
    c = k - p;
    e = k + j;
    f = n - j;
    d = p + r;
    b = l - n;
    a = p + r;
    b = l + l;
    b = r - q;
    b = j + r;
    f = p - n;
    b = p + m;
    e = l - q;
    h = j + m;
    g = l - l;
    a = m + m;
    b = k + k;
    a = j - l;
    m = q - o;
    d = p + n;
    d = m + q;
    h = q + q;
    d = p + p;
    b = l - k;
    g = p - q;
    g = n - k;
    f = j + p;
    d = k + q;
    h = o - q;
    e = n - r;
    h = n + r;
    e = p - q;
    f = k - p;
    h = j + o;
    d = k + j;
    f = k + k;
    b = l + m;
    i = n - j;
    e = n + m;
    a = m - q;
    f = k + l;
    f = k + b;
    c = l + o;
    g = l - p;
    a = i + p;
    h = k - m;
    g = j + l;
    a = l + j;
    e = q + m;
    c = k - k;
    d = j - r;
    c = n + j;
    o = q - m;
    d = j - r;
    a = o + r;
    i = q + q;
    f = l - q;
    b = l + r;
    a = m + r;
    d = l + q;
    i = r + q;
    d = k + q;
    b = l - j;
    a = r - m;
    i = m + k;
    d = l + n;
    a = p - l;
    g = r + m;
    d = m + l;
    b = p + n;
    d = j - l;
    b = q - p;
    e = k - p;
    b = o + p;
    e = r - l;
    h = r + n;
    g = q + r;
    a = m + n;
    h = k - p;
    e = k - o;
    h = p - p;
    g = p + p;
    i = q + k;
    c = l - j;
    i = n + m;
    i = p - l;
    a = l + l;
    c = p - n;
    i = k - m;
    g = l + o;
    d = p + q;
    e = j + r;
    a = j - k;
    b = p - q;
    a = n + o;
    g = m - r;
    b = o - j;
    e = m - p;
    b = n - n;
    g = l - j;
    h = o + o;
    e = q + j;
    c = j - q;
    d = j + a;
    c = o + q;
    d = o + p;
    b = m + j;
    e = q + p;
    b = m - n;
    f = o - l;
    h = q - p;
    a = k - p;
    c = q - r;
    d = j - j;
    d = q - k;
    c = j + p;
    d = n - l;
    h = o + k;
    c = p + q;
    f = m + q;
    d = n - m;
    e = l + m;
    h = r - k;
    c = k + o;
    h = n + j;
    d = n + p;
    f = k - j;
    b = n + j;
    g = m - l;
    f = r - l;
    d = m + r;
    i = r + l;
    i = n + n;
    h = j + n;
    h = j + r;
    a = p - n;
    a = m - l;
    g = l - j;
    h = q + o;
    g = r + r;
    d = m + k;
    h = m - l;
    c = r - p;
    b = n - r;
    f = m + n;
    d = r - j;
    e = j + k;
    d = q - m;
    g = l + r;
    e = k + p;
    e = j - n;
    f = j - q;
    // End optimization range
    return a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r;
}

int main() {
    srand (0);
    double a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r;  
    a= randfrom(-100.0, 100.0);
    b= randfrom(-100.0, 100.0);
    c= randfrom(-100.0, 100.0);
    d= randfrom(-100.0, 100.0);
    e= randfrom(-100.0, 100.0);
    f= randfrom(-100.0, 100.0);
    g= randfrom(-100.0, 100.0);
    h= randfrom(-100.0, 100.0);
    i= randfrom(-100.0, 100.0);
    j= randfrom(-100.0, 100.0);
    k= randfrom(-100.0, 100.0);
    l= randfrom(-100.0, 100.0);
    m= randfrom(-100.0, 100.0);
    n= randfrom(-100.0, 100.0);
    o= randfrom(-100.0, 100.0);
    p= randfrom(-100.0, 100.0);
    q= randfrom(-100.0, 100.0);
    r= randfrom(-100.0, 100.0);
    // Timer code from https://www.techiedelight.com/measure-elapsed-time-program-chrono-library/
    auto start = chrono::steady_clock::now();
    double res;
    for (int i = 0; i < 2000000; i++) {
        res = op_function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r);
    }
    auto end = chrono::steady_clock::now();
    cout << "Elapsed time in milliseconds: "
        << chrono::duration_cast<chrono::milliseconds>(end - start).count()
        << " ms" << endl;
    printf("hash: %f\n", res);
    return 0;
}

