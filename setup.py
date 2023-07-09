""" Setup file to make the content installable """
import setuptools

repo_url = "https://github.com/Jtachan/enigma_cypher.git"

if __name__ == "__main__":
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        url=repo_url,
        name="enigma-cypher",
        author="Jaime Gonzalez Gomez",
        author_email="jim.gomez.dnn@gmail.com",
        version="0.0.0",
        python_requires=">=3.8",
        description="Package providing encoder and decoder instances to use the "
                    "enigma machine cypher",
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=setuptools.find_namespace_packages(include=["enigma_cypher.*"]),
        namespace_packages=["enigma_cypher"],
        install_requires=[],
    )
