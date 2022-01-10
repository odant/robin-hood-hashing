from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
import shutil
import os

required_conan_version = ">=1.33.0"

class GoogleBenchmarkConan(ConanFile):
    name = "robin-hood-hashing"
    version = "3.11.4+0"
    description = "Fast & memory efficient hashtable based on robin hood hashing for C++11/14/17/20"
    url = "https://github.com/martinus/robin-hood-hashing"
    homepage = "https://github.com/martinus/robin-hood-hashing"
    author = "Martin Ankerl"
    license = "MIT License"
    exports_sources = ["*"]
    generators = "cmake"
    no_copy_source = True

    _cmake = None

    def source(self):
        # Wrap the original CMake file to call conan_basic_setup
        shutil.move("CMakeLists.txt", "CMakeListsOriginal.txt")
        shutil.move(os.path.join("conan", "CMakeLists.txt"), "CMakeLists.txt")

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake

        self._cmake = CMake(self)
        self._cmake.definitions["RH_STANDALONE_PROJECT"] = "OFF"
        self._cmake.configure()
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
