from setuptools import setup, find_packages

setup(
    name="mlproject",
    version="0.0.1",
    author="kolliPrudhvi",
    author_email="prudhvikolli123@gmail.com",
    package_dir={"": "src"},              # REQUIRED for src/mlproject
    packages=find_packages(where="src"),  # REQUIRED
    install_requires=[
        "pandas",
        "numpy",
        "seaborn",
        "scikit-learn",
    ],
)


