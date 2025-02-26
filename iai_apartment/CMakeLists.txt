cmake_minimum_required(VERSION 3.5)
project(iai_apartment)


find_package(ament_cmake REQUIRED)
find_package(xacro REQUIRED)


# Path to the Xacro file
set(XACRO_FILE ${CMAKE_CURRENT_SOURCE_DIR}/urdf/apartment.xacro)
set(URDF_FILE ${CMAKE_CURRENT_BINARY_DIR}/urdf/apartment.urdf)

# Generate URDF from Xacro
add_custom_command(
  OUTPUT ${URDF_FILE}
  COMMAND xacro ${XACRO_FILE} -o ${URDF_FILE}
  DEPENDS ${XACRO_FILE}
  COMMENT "Generating URDF from Xacro"
)

# Add custom target to trigger xacro
add_custom_target(xacro ALL DEPENDS ${URDF_FILE})

install(DIRECTORY urdf launch meshes rviz_config maps owl
  DESTINATION share/${PROJECT_NAME})

ament_package()