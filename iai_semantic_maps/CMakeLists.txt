cmake_minimum_required(VERSION 3.5)
project(iai_semantic_maps)

find_package(ament_cmake REQUIRED)

install(DIRECTORY owl prolog
  DESTINATION share/${PROJECT_NAME})

ament_package()