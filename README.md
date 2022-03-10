# GitPodExample
Example GitPod Environment

https://gitpod.io#https://github.com/calaldees/GitPodExample


Problem
-------

Teaching Computing is difficult in schools because the computers are often managed machines.
Young people are not allowed to install new software or libraries.
This makes education difficult.


Solution
--------

Use a remote development environment.
GitPod provides a cloud/browser based profetional development environment for free with a GitHub login.
(50 Hours free use every 30 days)
Students can install packages and run command line applications.
The state of workspace is from a GitHub repo. This allows a teacher to setup pre prepared resources.


Demo
----

This GitPod workspace is deliberatly bare-bones.
I want students/teachers to install packages manually. These can be added to be performed automatically to `.gitpod.yml` if needed.

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
python3 elevation.py
# view `elevation_uk.png` output
```
