# FUR HexChat addons

Plugin tries to remember case number and which case given client belongs to. Then plugin will annotate each chat line with the respective client name and case number if it can figure out which case does the message belong to.

Allows filtering by odd/even cases.

Also, contains a bunch of aliases by default.

Does not rely on bot/api functioning, can be used independently as long as associations are added-removed with commands.

**Warning:** case detection is not always 100% reliable.

## Installation

0. Backup your hexchat config dir.
0. Copy contents of the repo into your hexchat config dir with replacement.
0. Restart hexchat. 

## Commands reference

* `/fcs` - loads current cases from Mecha.
* `/fc 1 clientnick` - manually associates case number 1 with "clientnick".
* `/fcd 1` - removes case 1 association.
* `/fcd clientnick` - removes clientnick association.
* `/fcc` - lists currently known case numbers.

## Modes

Plugin can filter messages based on odd-even case number.

* `/fmode all` - will show all messages.
* `/fmode odd` - will output messages with odd case numbers only, or those with undetected case.
* `/fmode even` - will output messages with even case numbers only, or those with undetected case.

## Log

Sometimes filtering and/or highlighting can go wrong. All the messages are pasted as is into the "Log" tab of the hexchat, without any modifications. Please, remember to post relevant part of the log along with the issue.
