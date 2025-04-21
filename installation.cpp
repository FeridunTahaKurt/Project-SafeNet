#include <iostream>
#include <cstdlib>
#include <filesystem>
#include <string>

namespace fs = std::filesystem;

bool checkPythonInstalled() {
    int result = system("where python > nul 2>&1"); 
    return result == 0;
}

bool checkModuleInstalled(const std::string& module) {
    std::string command = "python -m pip list | findstr /i " + module + " > nul 2>&1";
    int result = system(command.c_str());
    return result == 0;
}

bool checkTorInstalled() {
    fs::path torPath = "C:\\Program Files\\Tor Browser\\Browser\\TorBrowser.exe"; /
    return fs::exists(torPath);
}

void downloadPython() {
    std::cout << "Python is not downloaded. Downloading..." << std::endl;
    system("start https://www.python.org/downloads/");
}

void downloadTor() {
    std::cout << "Tor Browwser is not downloaded. Downloading..." << std::endl;
    system("start https://www.torproject.org/download/");
}

int main() {
    // Python kontrolü
    if (!checkPythonInstalled()) {
        std::cout << "Python is not installed." << std::endl;
        downloadPython();
    } else {
        std::cout << "Python is already installed." << std::endl;

        // Python modül kontrolleri
        std::string modules[] = {"requests", "customtkinter"};
        for (const std::string& module : modules) {
            if (!checkModuleInstalled(module)) {
                std::cout << module << " Library is not downloaded. Downloading..." << std::endl;
                system(("python -m pip install " + module).c_str());
            } else {
                std::cout << module << " Library already installed." << std::endl;
            }
        }
    }

    // Tor Browser kontrolü
    if (!checkTorInstalled()) {
        std::cout << "Tor Browser is not downloaded." << std::endl;
        downloadTor();
    } else {
        std::cout << "Tor Browser is downloaded." << std::endl;
    }

    return 0;
}
