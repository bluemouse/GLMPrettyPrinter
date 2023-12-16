#include <iostream>
#include <string>
#include <vector>

#include <glm/glm.hpp>

#include <glm/gtx/string_cast.hpp>

#include <glm/ext/matrix_transform.hpp>

int main (int /* argc */, char** /* argv */) {

  // auto testVec2 = glm::vec2{1.1f, 2.2F};
  // std::cout << glm::to_string(testVec2) << std::endl;
  // auto testVec3 = glm::vec3{1.1f, 2.2F, 3.3F};
  // std::cout << glm::to_string(testVec3) << std::endl;
  // auto testVec4 = glm::vec4{1.1f, 2.2F, 3.3F, 4.4F};
  // std::cout << glm::to_string(testVec4) << std::endl;

  // auto testivec2 = glm::ivec2{1, 2};
  // std::cout << glm::to_string(testivec2) << std::endl;
  // auto testivec3 = glm::ivec3{1, 2, 3};
  // std::cout << glm::to_string(testivec3) << std::endl;
  // auto testivec4 = glm::ivec4{1, 2, 3, 4};
  // std::cout << glm::to_string(testivec4) << std::endl;

  // auto testbVec2 = glm::bvec2{true, false};
  // std::cout << glm::to_string(testbVec2) << std::endl;
  // auto testbVec3 = glm::bvec3{true, false, true};
  // std::cout << glm::to_string(testbVec3) << std::endl;
  // auto testbVec4 = glm::bvec4{true, false, true, false};
  // std::cout << glm::to_string(testbVec4) << std::endl;

  auto testdVec2 = glm::dvec2{1.1, 2.2};
  std::cout << glm::to_string(testdVec2) << std::endl;

  auto testuVec3 = glm::uvec3{1, 2, 3};
  std::cout << glm::to_string(testuVec3) << std::endl;

  glm::vec3 offset = glm::vec3{1.0f, 2.0F, 3.0F};
  std::cout << glm::to_string(offset) << std::endl;
  glm::mat4 identity = glm::mat4{1.0F};
  std::cout << glm::to_string(identity) << std::endl;

	glm::mat4 translation = glm::translate(identity, offset);
  std::cout << glm::to_string(translation) << std::endl;

  const glm::mat4 tt = translation;
  std::cout << glm::to_string(tt) << std::endl;

  std::cout << std::endl;
}