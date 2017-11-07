cmake_minimum_required(VERSION 3.2)
project(leetcodes)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES Count_Complete_Tree_Nodes.cpp)
add_executable(leetcodes ${SOURCE_FILES})
