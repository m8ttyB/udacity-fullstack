Tournament Results - Swis System Tournament
--------------------------------------------

This is project 2 (p2) of Udacity's Full Stack Web Developer Nanodegree class.

Unlike an [elimination style tourament], the [Swiss style tournament] tournament enables each
contestant to continue playing until a winner emerges.

In a Swiss tournament, players are matched against opponents that have similar scores.

For example:

_round 1_

* John vs Jane
* Sue vs Shaun

Jane and Shaun win their matches.
John and Sue lose their matches.

_round 2_

* Jane vs Shaun
* John vs Sue

Jane and John win their matches. The tournament is complete, Jane is our overall winner.

_final standings_

* Jane 2:0
* Shawn 1:1
* John 1:1
* Sue 0:2

[elimination style tournament]: https://en.wikipedia.org/wiki/Single-elimination_tournament
[Swiss style tournament]: https://en.wikipedia.org/wiki/Swiss-system_tournament

Prerequisites:

- [Vagrant] installed.
- [Python 2.7] installed.

[Vagrant]: https://www.vagrantup.com/
[Python2.7]: http://www.python.org/download/releases/2.6.8/

Quick Start:

- After cloning this repository and installing the prequisites, run 'cd vagrant`, `vagrant up`, and `vagrant ssh`.
- Once you are ssh'd into the VM, we need to create the `tournament` database. 
`cd /vagrant/tournament/ && psql`, lastly run `\i tournament.sql`. 
- Once the database and it's tables have successfullly been created, exit psql, `ctrl-d`.
- Ensure [bleach] is installed in the VM, run `sudo pip install -U bleach`.
- The last step is to run the tests, from the bash terminal in the VM, run `python tournament_test.py`.