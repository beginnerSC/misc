%module lib_swig
%{
#include "lib_swig.h"
%}
#define __version__ "0.0.1";
double square(double x);
double cube(double x);