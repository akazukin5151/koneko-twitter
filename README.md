# koneko-twitter

A minimal example of how [koneko](https://github.com/twenty5151/koneko) can be modified for other purposes. Here, twitter is used as an example.

![preview](preview.png)

A diff file is automatically generated for convenience as [patch.diff](patch.diff).

# Installation

```sh
git clone https://github.com/twenty5151/koneko-twitter.git
cd koneko-twitter
./patcher.sh
cd build/koneko
python setup.py develop
```

Run with `koneko_twitter`, enter `1` and a twitter username. Pages aren't supported in this example, due to the "infinite" scroll nature of twitter, and the twitter api I'm using.
