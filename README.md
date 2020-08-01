# koneko-twitter

A rough and minimal example of how [koneko](https://github.com/twenty5151/koneko) can be modified for other purposes. Here, twitter is used as an example.

![preview](preview.png)

A diff file is automatically generated for convenience as [patch.diff](patch.diff). Note that it clones to commit [3fd60163972ef1e97f8c7af354847d23c460d8ff](https://github.com/twenty5151/koneko/commit/3fd60163972ef1e97f8c7af354847d23c460d8ff), which is around the time when this patcher was made. The patcher might fail with the up-to-date repo at koneko because of various changes.

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

# License notes

While this repo (koneko-twitter) is licensed under the Mozilla Public License, the base koneko repo (used here by the patcher) is still licensed under GPLv3. Any direct changes to koneko (ie, `build/koneko/`), even if the repo was cloned by the patcher script, still falls under the GPL. Does changes made by the patcher trigger the GPL? Not a lawyer, but I think if your patches (licensed under MPL) is not standalone ("combined in a way that would make them effectively a single program"), then the GPL kicks in. So you can't use this MPL-licensed repo to circumvent the GPL, by making MPL-licensed-patches to a GPL-program.

**TLDR:** Everything that is initially cloned by you, such as the modified python files and the patcher script, is licensed under the MPL. The `koneko` repo that the patcher clones (when you run the patcher), is licensed under the GPL. Finally, I think you cannot make a completely new app based on koneko by using patches licensed under the MPL -- it must be released under GPLv3. 


