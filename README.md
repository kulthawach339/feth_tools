# feth_tools
# For most projects, this workflow file will not need changing; you simply need
# to commit it to your repository.
#
# You may wish to alter this file to override the set of languages analyzed,
# or to provide custom queries or build logic.
name: "CodeQL"

on:
  push:
    branches: [main, dev_*]
  pull_request:
    # The branches below must be a subset of the branches above
    branches: [main, dev_*]
  schedule:
    - cron: '0 7 * * 0'

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest

    strategy:
      fail-fast: false
      matrix:
        # Override automatic language detection by changing the below list
        # Supported options are ['csharp', 'cpp', 'go', 'java', 'javascript', 'python']
        language: ['python']
        # Learn more...
        # https://docs.github.com/en/github/finding-security-vulnerabilities-and-errors-in-your-code/configuring-code-scanning#overriding-automatic-language-detection

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2.4.0

    # Initializes the CodeQL tools for scanning.
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v1
      with:
        languages: ${{ matrix.language }}
        # If you wish to specify custom queries, you can do so here or in a config file.
        # By default, queries listed here will override any specified in a config file. 
        # Prefix the list here with "+" to use these queries and those in the config file.
        # queries: ./path/to/local/query, your-org/your-repo/queries@main

    # Autobuild attempts to build any compiled languages  (C/C++, C#, or Java).
    # If this step fails, then you should remove it and run the build manually (see below)
    - name: Autobuild
      uses: github/codeql-action/autobuild@v1

    # ℹ️ Command-line programs to run using the OS shell.
    # 📚 https://git.io/JvXDl

    # ✏️ If the Autobuild fails above, remove it and uncomment the following three lines
    #    and modify them (or add more) to build your code if your project
    #    uses a compiled language

    #- run: |
    #   make bootstrap
    #   make release

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v1
