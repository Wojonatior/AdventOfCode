cmake_minimum_required(VERSION 3.6)
project(cppSolutons)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp day1.cpp day1.h day2.cpp day2.h day3.cpp day3.h day6.h day6.cpp day7.cpp day7.h)
add_executable(cppSolutons ${SOURCE_FILES})