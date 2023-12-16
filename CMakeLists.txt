cmake_minimum_required(VERSION 3.27)

project(GLMPrettyPrinter)

find_package(glm REQUIRED)

add_executable(${PROJECT_NAME} testbed.cpp)

set_target_properties(${PROJECT_NAME} PROPERTIES
  CXX_STANDARD 20
)

target_link_libraries(${PROJECT_NAME}
  PRIVATE
    glm::glm
)

target_compile_options(${PROJECT_NAME}
  PRIVATE
    -Wall -Wextra -Wpedantic -Werror
)
