cmake_minimum_required(VERSION 3.5)
project(iai_kitchen_defs)

find_package(ament_cmake REQUIRED)

install(DIRECTORY def Media room
  DESTINATION share/${PROJECT_NAME})

ament_package()