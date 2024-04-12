// expected to replace: 843
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

double op_function(double a, double b, double c, double d, double e, double f, double g, double h) {
  // Start optimization range
    c = h - f;
    c = e + h;
    a = f + h;
    a = f - e;
    d = g - h;
    b = h - f;
    a = e + h;
    d = f - f;
    b = f + h;
    d = e + h;
    c = f - h;
    d = f - f;
    a = g - f;
    d = f - g;
    c = e - f;
    b = h - f;
    b = c - f;
    c = e + f;
    b = g + f;
    b = e - h;
    b = h + f;
    b = g + g;
    d = f - e;
    c = g + g;
    c = f - h;
    b = g + f;
    d = g - f;
    b = h + a;
    c = f - h;
    b = h + e;
    b = e - h;
    d = e - g;
    a = g + e;
    d = e - f;
    c = h + h;
    d = h + h;
    a = h + g;
    a = f + h;
    c = h - f;
    a = h - f;
    b = f + e;
    c = f + e;
    c = f - e;
    d = e - h;
    b = f + f;
    b = e + e;
    b = g + g;
    b = b + e;
    c = h - g;
    b = f + e;
    b = h - g;
    d = e + e;
    c = e - h;
    a = g - e;
    a = e + f;
    a = h + h;
    d = f + g;
    d = e + h;
    a = h - f;
    d = g - f;
    c = h - f;
    d = g + f;
    a = h - e;
    a = f - g;
    b = f - e;
    d = h + f;
    b = h + e;
    b = h + g;
    d = h + g;
    b = g + f;
    d = f - g;
    d = h + e;
    a = g + g;
    a = g - g;
    a = g + h;
    b = h - f;
    c = g - f;
    d = e - g;
    d = g + h;
    d = h + g;
    d = f + e;
    a = g - e;
    b = e - e;
    a = h - f;
    b = h - f;
    h = f + e;
    d = g + f;
    c = f - g;
    b = e - h;
    d = h - d;
    b = f + e;
    d = g + f;
    a = h - g;
    b = e - g;
    b = e + e;
    b = e + f;
    a = g - g;
    a = e - f;
    b = f - f;
    a = f - e;
    c = e - f;
    b = e - f;
    b = g - f;
    b = f - f;
    c = h + h;
    a = f + g;
    b = f + h;
    d = e - h;
    c = f - g;
    b = f + h;
    b = e + e;
    d = e - g;
    b = f - g;
    d = f + h;
    c = g + g;
    b = f - e;
    b = f + e;
    b = f + e;
    b = e - h;
    b = h - f;
    d = g + g;
    d = h + b;
    b = f + g;
    d = h + f;
    d = f + h;
    d = h - e;
    c = h + h;
    d = f + e;
    a = e + h;
    a = f + h;
    a = h - h;
    c = f - g;
    b = f + f;
    a = f + e;
    b = f - e;
    a = g - e;
    a = h - e;
    a = f + h;
    d = e + g;
    a = e + f;
    c = h - g;
    d = e - g;
    b = e + h;
    a = g + h;
    a = h - e;
    c = f + f;
    f = h - g;
    b = f + h;
    b = f - e;
    c = h - g;
    e = g + f;
    a = e - e;
    a = e + f;
    b = e + f;
    c = e + f;
    c = f + g;
    c = h - g;
    a = h + f;
    d = e + f;
    d = g - h;
    a = e + f;
    c = g + h;
    d = h - g;
    d = f + e;
    b = e + h;
    a = f + f;
    d = e + h;
    b = e + g;
    d = h + e;
    b = f - f;
    d = g - e;
    b = e - g;
    b = f - f;
    c = h + e;
    a = e - g;
    b = f + e;
    b = g + f;
    c = f - g;
    c = h + e;
    c = h - f;
    d = e - g;
    d = g - f;
    d = g - e;
    c = e - h;
    d = h + g;
    a = f + h;
    c = g + h;
    d = h - f;
    d = g + f;
    d = g + e;
    a = g + g;
    a = e - g;
    d = g + f;
    d = g + g;
    c = f + e;
    a = h - e;
    a = h - g;
    a = e - f;
    d = g - e;
    d = e + f;
    b = h + f;
    d = g + e;
    b = h + f;
    c = h - f;
    b = e + f;
    c = f - h;
    d = g + h;
    a = h - e;
    d = f + e;
    b = f + f;
    d = e - g;
    c = e + e;
    b = g - g;
    b = g + h;
    b = e + f;
    d = e + g;
    a = h + h;
    c = g + g;
    b = g + e;
    b = f + f;
    a = e + e;
    a = h - f;
    d = g + h;
    a = g - e;
    c = g - f;
    a = g + f;
    a = h - g;
    d = f + f;
    d = e - g;
    a = h - g;
    c = h + h;
    b = f - h;
    d = g + g;
    d = g - f;
    c = e + h;
    b = e + f;
    a = f - f;
    d = h - h;
    c = h - e;
    d = g - h;
    d = f + g;
    c = f - e;
    a = e + h;
    c = f + f;
    c = h - g;
    b = e + h;
    a = g + g;
    c = e - e;
    a = h + e;
    d = f + h;
    a = e - e;
    c = f + h;
    a = f - g;
    a = g + e;
    d = h + f;
    c = e + e;
    b = g - g;
    d = e - f;
    d = e - f;
    a = f - e;
    c = e - h;
    a = e - f;
    a = g - h;
    b = f + e;
    d = e - g;
    a = g - f;
    a = g + e;
    d = e - h;
    d = c - e;
    d = e + e;
    c = g - g;
    d = e + f;
    c = f + g;
    b = e - g;
    c = f + h;
    b = h + e;
    b = h + h;
    b = c - g;
    d = f + f;
    d = f - h;
    b = f + h;
    b = h - e;
    a = g - h;
    c = e - e;
    a = g + e;
    a = g + f;
    b = f - e;
    c = h - e;
    a = h + g;
    b = g - g;
    c = e + f;
    b = f - g;
    d = f - g;
    a = h + h;
    b = f - h;
    d = f - h;
    b = g - f;
    a = h - f;
    b = e - e;
    d = e + g;
    b = f - e;
    a = f - h;
    b = f + f;
    c = f + f;
    a = f + e;
    a = h + h;
    a = g + f;
    d = f - h;
    d = d - e;
    b = f + c;
    a = f + f;
    a = f + e;
    a = e + f;
    d = b + g;
    c = h - g;
    b = e - h;
    b = g - e;
    d = f + g;
    a = e - f;
    b = f + e;
    b = f + f;
    a = g + f;
    b = f - h;
    d = h - h;
    a = h - g;
    a = h + g;
    c = g - h;
    d = f - g;
    a = h + g;
    c = e + e;
    c = f - h;
    c = g - e;
    c = c - h;
    a = g - h;
    a = h + g;
    a = g + b;
    c = f - g;
    a = h + g;
    a = h + g;
    c = e - e;
    a = e + f;
    a = f + g;
    b = h + f;
    c = g - f;
    c = h - g;
    a = e + f;
    c = f + g;
    a = f + h;
    b = h + h;
    d = e - g;
    h = g - g;
    c = e - h;
    d = e - f;
    b = g - e;
    b = g - h;
    c = g - f;
    c = f - e;
    b = g + f;
    d = g + f;
    a = h + g;
    a = e - f;
    d = h + g;
    c = f - e;
    c = g + g;
    b = e + e;
    c = f + f;
    d = e - f;
    a = e + f;
    b = e - e;
    a = f - g;
    c = g + g;
    b = f - f;
    a = g + h;
    d = h + f;
    d = e + f;
    c = e - g;
    d = f + e;
    d = f + f;
    a = g - f;
    d = b + g;
    d = f + g;
    c = f + g;
    b = e + h;
    a = h + e;
    c = f + h;
    b = e - f;
    d = h - e;
    c = g + g;
    c = d - h;
    a = h + h;
    a = h - f;
    a = g + g;
    b = g + g;
    c = g + h;
    c = g - h;
    c = h + g;
    d = e - g;
    b = e - g;
    b = e + f;
    b = c - h;
    a = f - e;
    c = g + g;
    b = h + f;
    a = e + g;
    c = g + h;
    a = h + g;
    d = f + f;
    d = f + f;
    d = h + e;
    d = h - g;
    c = f + g;
    b = f - e;
    e = e - h;
    d = f - f;
    b = g - e;
    c = g - g;
    d = e + f;
    c = e + g;
    d = h - g;
    b = f - g;
    b = f - g;
    b = c + g;
    b = e + g;
    d = e - e;
    c = g - e;
    c = f + a;
    d = f - f;
    d = f - e;
    b = f + f;
    c = h + f;
    a = f - f;
    c = f + h;
    b = f - e;
    c = g - g;
    d = h - f;
    d = f + f;
    b = h + e;
    d = e - h;
    b = e - e;
    d = h + f;
    d = h - g;
    a = e - e;
    d = h - g;
    c = e - h;
    d = g - g;
    d = h - f;
    c = f + h;
    c = g + h;
    c = g + f;
    b = e - f;
    c = h + f;
    a = h - g;
    a = f - h;
    c = h + f;
    c = g - h;
    d = g + e;
    a = e - h;
    a = g - e;
    d = h + g;
    d = g - g;
    b = f - h;
    a = g - e;
    c = g - d;
    b = e - h;
    b = e - f;
    b = g - e;
    c = g - e;
    a = h - e;
    d = g - g;
    d = h + h;
    d = e - e;
    d = f - h;
    b = h - e;
    d = g - f;
    c = f - e;
    b = f + h;
    d = e + h;
    d = g + f;
    d = e - f;
    b = f + e;
    b = f - f;
    a = f + h;
    h = e + h;
    b = g + h;
    c = e - e;
    c = g + g;
    a = f + h;
    b = e - g;
    c = f - h;
    a = h - g;
    c = e + f;
    a = h + f;
    b = h + f;
    d = h - g;
    c = h - g;
    d = h + f;
    d = e + e;
    c = e - h;
    d = h + h;
    a = h + h;
    c = g - g;
    a = h - f;
    c = e - h;
    c = h - g;
    c = h - e;
    b = e - h;
    c = e - f;
    a = e - f;
    c = f + h;
    d = e + h;
    a = e + g;
    d = g - h;
    a = g - g;
    b = f + e;
    a = e - e;
    d = f - h;
    b = e + g;
    d = g + e;
    b = e + g;
    c = g - g;
    b = g + h;
    d = g + g;
    a = g + h;
    c = h - g;
    c = f - e;
    b = h + g;
    c = g - h;
    c = e + f;
    b = b - e;
    d = h - g;
    c = f + h;
    b = h + g;
    c = h - g;
    d = h + h;
    c = h + g;
    c = h + h;
    c = e - g;
    b = g + g;
    c = e - g;
    a = e - f;
    c = e + f;
    h = h - g;
    b = g + g;
    a = g - h;
    b = g - e;
    d = h - f;
    a = e + f;
    b = e + e;
    b = g - e;
    a = f + g;
    b = f - f;
    c = e - g;
    d = f + g;
    c = h - h;
    b = h - f;
    a = g + e;
    a = h - e;
    c = f + f;
    c = f + h;
    b = g - g;
    b = e - h;
    d = f + g;
    b = g + f;
    d = g + e;
    b = g + f;
    b = e - g;
    c = f - e;
    a = e + f;
    a = h - h;
    c = e - g;
    a = g + h;
    c = e + h;
    d = e - g;
    a = g + f;
    a = g + f;
    d = g - h;
    d = g + f;
    c = e + e;
    b = e + e;
    a = e - h;
    c = h + g;
    a = f + g;
    a = f + e;
    a = f - e;
    a = g - h;
    d = e - h;
    b = e - e;
    a = f - g;
    a = g + e;
    a = h - g;
    b = h - g;
    b = h - f;
    a = f + h;
    c = e - h;
    b = g + e;
    d = g - g;
    c = e + e;
    a = e - f;
    b = h - f;
    d = g + f;
    a = f + h;
    b = h - e;
    c = h + f;
    a = g + g;
    c = h - h;
    a = h + e;
    d = f - f;
    c = g + e;
    c = f - e;
    d = f - g;
    c = h + g;
    a = e + e;
    a = f - g;
    c = h - f;
    a = g + h;
    d = g + e;
    c = e + g;
    b = f - g;
    b = h + g;
    a = g - e;
    d = g + e;
    b = e + b;
    b = g - g;
    a = h - g;
    a = f + g;
    b = h - e;
    d = h + e;
    c = e + g;
    c = h + g;
    a = f - e;
    c = e - g;
    b = h + h;
    c = e + f;
    b = e + e;
    c = h + e;
    d = f - g;
    b = h + f;
    c = g - g;
    c = f + h;
    a = g - f;
    b = h + e;
    c = g - h;
    a = e + e;
    a = h - g;
    c = f - e;
    a = b - e;
    d = h + g;
    c = g - g;
    a = f - e;
    c = b - g;
    c = f + f;
    b = g - f;
    b = h + h;
    d = h - h;
    c = f - e;
    c = f - h;
    d = g + e;
    d = h + f;
    a = f - h;
    c = h - h;
    b = g + f;
    c = g - h;
    d = e + h;
    c = f - g;
    b = f - f;
    c = e - e;
    c = e - e;
    d = h + e;
    c = f - g;
    a = e + e;
    c = h - f;
    c = h - e;
    b = g + g;
    c = g + g;
    d = e + e;
    c = g - g;
    c = g + e;
    a = f + e;
    b = e - g;
    a = g - g;
    b = g + g;
    c = g + g;
    d = f + h;
    b = g + h;
    a = h + e;
    b = e + f;
    b = f + f;
    a = g - e;
    d = g + h;
    b = c + d;
    a = g - f;
    a = e + g;
    d = f - h;
    d = h - g;
    c = g + g;
    c = f - h;
    c = f + e;
    b = g - g;
    c = g + e;
    a = h - h;
    a = g + f;
    b = g - f;
    c = h - f;
    c = h + h;
    a = g - e;
    c = g - g;
    d = g - g;
    c = g - f;
    a = g + e;
    b = e + h;
    d = g + g;
    d = f - h;
    c = g + h;
    c = f - f;
    f = f - f;
    a = g + e;
    b = h + h;
    d = e + h;
    d = e - e;
    b = h + e;
    c = h + e;
    b = e - g;
    c = f - e;
    d = h - f;
    c = g + g;
    a = f + h;
    b = f + e;
    a = h + h;
    c = g + f;
    c = e - e;
    d = e - e;
    a = h + h;
    d = e - h;
    b = f - f;
    c = f - h;
    c = f - g;
    b = e - h;
    c = g - f;
    b = g - f;
    c = g - g;
    c = f - e;
    d = f + h;
    a = f - g;
    d = e + h;
    a = h + g;
    a = e - f;
    b = g + e;
    b = e - h;
    a = e - g;
    a = g - c;
    b = h + e;
    c = e - f;
    a = e - f;
    b = g - f;
    c = f + h;
    d = h + e;
    a = h - f;
    b = h - h;
    a = e + g;
    a = h + g;
    a = g + g;
    b = h - f;
    d = f + e;
    d = h - g;
    c = g - g;
    d = f - g;
    a = g - h;
    d = h - e;
    d = h - f;
    d = e - h;
    a = f - f;
    a = e + g;
    a = f + e;
    d = h + h;
    a = h + h;
    b = f - h;
    a = h + f;
    a = e - e;
    a = e + h;
    c = f - e;
    b = h - e;
    d = e + e;
    b = e + f;
    d = e - g;
    a = e + g;
    d = f - f;
    b = e + h;
    a = h + f;
    d = g - h;
    c = e + g;
    a = g - g;
    a = g + g;
    d = h - g;
    a = e - g;
    c = g - h;
    d = f - h;
    d = e + g;
    d = f - g;
    b = e - f;
    c = h + f;
    c = h - f;
    b = e + h;
    d = f + h;
    c = e - e;
    d = f - g;
    d = g - f;
    c = f - h;
    d = g + f;
    a = e + e;
    c = e + e;
    d = h - e;
    d = e + g;
    c = h + f;
    d = b - g;
    d = e - g;
    a = b - e;
    a = e + e;
    b = g + h;
    c = h - h;
    b = g + f;
    a = h - e;
    b = f - e;
    a = e + h;
    b = g + e;
    c = g - e;
    d = h - h;
    a = g - h;
    c = f + g;
    b = h + f;
    c = e + f;
    d = g - g;
    c = f + h;
    c = g - e;
    a = h + g;
    a = e - h;
    g = e - e;
    a = h - e;
    c = g - f;
    a = h - f;
    d = f - e;
    c = f - e;
    b = e + e;
    d = g - g;
    d = g - e;
    b = f + g;
    d = h + h;
    d = g - h;
    c = g + g;
    a = d - e;
    d = g + h;
    d = f - h;
    d = f + g;
    e = f - e;
    c = g + h;
    a = f - h;
    c = f - g;
    a = h + g;
    d = f - g;
    a = h + f;
    b = h - g;
    a = f + g;
    b = f - f;
    c = e + g;
    b = h + f;
    a = g + g;
    d = g + e;
    a = g + e;
    b = g - h;
    a = f + e;
    a = f - e;
    a = h - e;
    d = g + f;
    d = e - g;
    d = g + g;
    d = g - h;
    d = g - h;
    a = h - h;
    a = e + g;
    c = f + e;
    d = e - f;
    d = g + f;
    c = h - e;
    d = g + e;
    a = g + f;
    b = h - f;
    b = g - e;
    c = h + g;
    b = g + f;
    c = g - g;
    c = h - e;
    a = g + f;
    a = f - f;
    a = f - f;
    a = f + g;
    b = f - g;
    a = e + f;
    a = e + h;
    a = g - g;
    b = h - h;
    a = h + e;
    c = h + g;
    a = g - f;
    d = h + e;
    b = e - f;
    b = e + f;
    a = f + g;
    a = f + h;
    b = e + g;
    b = g + e;
    b = g + e;
    d = g - f;
    c = h - f;
    b = h - g;
    c = h - g;
    d = e - e;
    d = g - g;
    a = f + f;
    a = e + f;
    d = g - h;
    c = g - e;
    a = e + f;
    b = h - e;
    b = f - g;
    d = g - e;
    a = d + f;
    d = e - g;
    b = f - e;
    d = g + g;
    d = g + h;
    b = e - g;
    b = g + f;
    d = h + g;
    a = f - g;
    a = e - h;
    b = h - e;
    c = f + f;
    b = h - g;
    c = f - h;
    c = g + g;
    d = e - f;
    b = e - f;
    b = g - e;
    b = h - g;
    a = e - g;
    a = e + f;
    a = e + f;
    b = e + f;
    c = e - h;
    d = g - h;
    b = f + h;
    b = f + f;
    d = h - g;
    c = h - f;
    c = f - e;
    c = g - g;
    a = h - e;
    b = f + h;
    b = e + g;
    d = h + f;
    b = f - h;
    a = e - g;
    d = f + f;
    b = g - h;
    d = f - g;
    b = h + e;
    c = h - e;
    b = f - f;
    c = f - e;
    d = e + d;
    a = h - h;
    d = f - f;
    d = f + e;
    c = g - g;
    d = g - h;
    d = f - e;
    d = h + h;
    c = f - e;
    d = e - h;
    a = e - g;
    d = h + g;
    a = g - f;
    b = h - e;
    d = h - f;
    a = g + e;
    a = g + h;
    c = g + f;
    b = f - f;
    c = g - h;
    c = e + f;
    b = g - e;
    a = h + h;
    a = e - h;
    a = e + e;
    b = f + f;
    c = h + g;
    a = f + g;
    a = e - f;
    c = e + e;
    b = h - e;
    c = f - h;
    // End optimization range
    return a+b+c+d+e+f+g+h;
}

int main() {
    srand (0);
    double a,b,c,d,e,f,g,h;  
    a= randfrom(-100.0, 100.0);
    b= randfrom(-100.0, 100.0);
    c= randfrom(-100.0, 100.0);
    d= randfrom(-100.0, 100.0);
    e= randfrom(-100.0, 100.0);
    f= randfrom(-100.0, 100.0);
    g= randfrom(-100.0, 100.0);
    h= randfrom(-100.0, 100.0);
    // Timer code from https://www.techiedelight.com/measure-elapsed-time-program-chrono-library/
    auto start = chrono::steady_clock::now();
    double res;
    for (int i = 0; i < 2000000; i++) {
        res = op_function(a,b,c,d,e,f,g,h);
    }
    auto end = chrono::steady_clock::now();
    cout << "Elapsed time in milliseconds: "
        << chrono::duration_cast<chrono::milliseconds>(end - start).count()
        << " ms" << endl;
    printf("hash: %f\n", res);
    return 0;
}

