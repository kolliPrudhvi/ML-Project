from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path):
    requirements = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if line and line != HYPHEN_E_DOT:
                requirements.append(line)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="kolliPrudhvi",
    author_email="prudhvikolli123@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)



