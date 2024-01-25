## PIR experiment

<br>


Install dependencies:

```bash
python3 -m venv venv
source ./venv/bin/activate
make install_deps
```

Add config and LWE parameters to:

```bash
cp .env.example .env
vim .env
```

Run:

```bash
make install
```


Test your installation:

```
pir

usage: pir [-h] [-e] [-s] [-a] [-i] [-t] [-p]

options:
  -h, --help  show this help message and exit
  -e          Run simple linear key Regev encryption experiment with sampled error. Example: pir -e
  -s          Run simple linear key Regev encryption experiment with scaled msg. Example: pir -s
  -a          Prove that the Regev scheme is additive homomorphic. Example: pir -s
  -i          Prove that the Regev scheme supports plaintext inner product. Example: pir -i
  -t          Run a very simple PIR explanation (without encryption). Example: pir -t
  -p          Run a secret key Regev PIR experiment. Example: pir -p
```


<br>
