# VSCodeOnlineExample
Example CodeSpaces/GitPod Environment


Problem
-------

Teaching Computing is difficult in schools because the computers are often managed machines.
Young people are not allowed to install new software or libraries.
This makes education difficult.


Solution
--------

* Use a remote development environment
* Cloud/Browser based professional development environment (VisualStudioCode) for free with a GitHub login
    * (50 Hours free use every 30 days)
* Students can install packages and run command line applications
* The state of workspace is from a GitHub repo
    * This allows a teacher to setup pre prepared resources

Use
---

* Cloud VSCode IDE
    * GitHub CodeSpaces
        * [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/calaldees/VSCodeOnlineExample?quickstart=1)
            * https://codespaces.new/USERNAME/REPO?quickstart=1
        * Manage: https://github.com/codespaces/
        * Shutdown: `gh cs stop`
        * Delete: `gh cs delete`
        * Advanced Config (Startup): `.devcontainer/devcontainer.json`
        * Issues:
            * Ports need to be set to `public` manually (this can't be automated and is tedious)
                * [Allow for ports to be public by default #4068](https://github.com/orgs/community/discussions/4068)
                * `gh codespace ports visibility 8000:public -c $CODESPACE_NAME`
    * GitPod
        * [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/calaldees/VSCodeOnlineExample)
            * https://gitpod.io/#https://github.com/USERNAME/REPO
        * Manage: https://gitpod.io/workspaces
        * Shutdown: `gp stop`
        * Delete: `gp ???`
        * Advanced Config (Startup): `.gitpod.yml`
        * Issues:
            * `git push` wont work until permissions are set 
                * [GitPod: granting-additional-github-oauth-permissions](https://www.gitpod.io/docs/configure/authentication/github#granting-additional-github-oauth-permissions)
                    * `public_repo`, `repo` and `workflow`
* Remember to stop your workspace manually to save hours



Demo
----

* This GitPod workspace example is deliberately bare-bones
* I want students/teachers to
    * manually install packages
    * manually running the web-server
        * This is a transferable concept/skill
    * These can be added to be performed automatically to  if desired for younger students


### Example: Plotly

```bash
pip install plotly
python3 plotly_demo.py
python3 -m http.server
# view `basic-line.html`
```

### Exanple: Pillow

```bash
curl  -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" -O "https://shadedrelief.com/natural3/ne3_data/8192/elev_bump_8k.jpg"
pip install pillow
python3 elavation.py
# view `elevation_uk.png` output
```


Future Ideas
------------

* Login is difficult for children - SSO could solve this?
* [GitHub Campus](https://education.github.com/partner_school_applications/apply) might be free for schools?
