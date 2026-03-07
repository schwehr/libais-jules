# -*- shell-script -*- make up a mode for emacs

# To use cmake:
#
# cmake .
# make

cmake_minimum_required(VERSION 3.25)
project (
  libais
  DESCRIPTION "A library for parsing Automatic Identification System messages."
  LANGUAGES CXX
  VERSION 0.17
)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# include_directories("${PROJECT_BINARY_DIR}/src/libais")

add_subdirectory(src)

