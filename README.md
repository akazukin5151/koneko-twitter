# koneko-twitter

A rough and minimal example of how [koneko](https://github.com/twenty5151/koneko) can be modified for other purposes. Here, twitter is used as an example.

![preview](preview.png)

A diff file is automatically generated for convenience as [patch.diff](patch.diff).

# Installation

```sh
git clone https://github.com/twenty5151/koneko-twitter.git
cd koneko-twitter
./patcher.sh -c  # Short for --clone
cd build/koneko
python setup.py develop
```

Run with `koneko_twitter`, enter `1` and a twitter username. Pages aren't supported in this example, due to the "infinite" scroll nature of twitter, and the twitter api I'm using.

# Develop

* Edit the files
* If needed, copy `.py` files from `koneko` to root and edit them
* Finally run `./patcher.sh`
    * Without the clone option, the patcher just moves the files
* Test with `koneko_twitter` (assuming it is already installed with `python setup.py develop`)

Finally, you should run `./patcher.sh -c` for a clean build plus patch. A diff file will also be generated.

