# Yu-Gi-Oh! Forbidden and Limited List tracker

This little program will allow you to view the ygo banlist right in your terminal.

## Features

-   Listing: List the contents of the list in two formats, table and json
-   Filtering: Get the entire list or filter through it based on the following criteria:
    -   Diff, get only what changed on the newest list,
    -   Forbidden, get only the newly forbidden cards,
    -   Limited, get only the newly limited cards,
    -   Semi-Limited, get only the newly semi-limited cards,
    -   Unlimited, get only the cards that are now off the list
-   Caching: The program will cache the results so it doesn't have to process them every time it is ran

## Usage

You can see a comprehensive list of all the options by running the help command.

```shell
ygo-fll -h
```

## Examples

As an example you can opt to see the changes from the previous list by running the diff command.

```shell
ygo-fll -d
```

Long options are also supported.

```shell
ygo-fll --diff
```

Example output:

```
   Card Type             Card Name           Advanced Format   Traditional Format       Remarks
====================================================================================================
Monster/Link      Union Carrier              Forbidden         Limited              New
Monster/Xyz       Number S0: Utopic ZEXAL    Forbidden         Limited              New
Monster/Xyz       True King of All           Forbidden         Limited              New
                  Calamities
Monster/Ritual    Cyber Angel Benten         Limited           Limited              New
Monster/Effect    Dragon Buster              Unlimited         Unlimited            Was Forbidden
                  Destruction Sword
Monster/Link      Firewall Dragon            Unlimited         Unlimited            Was Forbidden
Monster/Link      The Phantom Knights of     Unlimited         Unlimited            Was Limited
                  Rusty Bardiche
Monster/Synchro   Dewloren, Tiger King of    Unlimited         Unlimited            Was Limited
                  the Ice Barrier
Monster/Synchro   Ignister Prominence, the   Unlimited         Unlimited            Was Limited
                  Blasting Dracoslayer
Spell             Rank-Up-Magic Argent       Unlimited         Unlimited            Was Forbidden
                  Chaos Force
Trap              True King’s Return         Unlimited         Unlimited            Was Semi-Limited

```

You can chain the output format option to any command to select a different output format.
The default is table, but json is also available.

```shell
ygo-fll -o json
```

Once again, long options are also supported.

```shell
ygo-fll --diff --output-format=json
```

Example output:

```
[
    {
        "card_type": "Monster/Link",
        "card_name": "Union Carrier",
        "advanced_format": "Forbidden",
        "traditional_format": "Limited",
        "remarks": "New"
    },
    {
        "card_type": "Monster/Xyz",
        "card_name": "Number S0: Utopic ZEXAL",
        "advanced_format": "Forbidden",
        "traditional_format": "Limited",
        "remarks": "New"
    },
    {
        "card_type": "Monster/Xyz",
        "card_name": "True King of All Calamities",
        "advanced_format": "Forbidden",
        "traditional_format": "Limited",
        "remarks": "New"
    },
    {
        "card_type": "Monster/Ritual",
        "card_name": "Cyber Angel Benten",
        "advanced_format": "Limited",
        "traditional_format": "Limited",
        "remarks": "New"
    },
    {
        "card_type": "Monster/Effect",
        "card_name": "Dragon Buster Destruction Sword",
        "advanced_format": "Unlimited",
        "traditional_format": "Unlimited",
        "remarks": "Was Forbidden"
    },
    {
        "card_type": "Monster/Link",
        "card_name": "Firewall Dragon",
        "advanced_format": "Unlimited",
        "traditional_format": "Unlimited",
        "remarks": "Was Forbidden"
    },
    {
        "card_type": "Monster/Link",
        "card_name": "The Phantom Knights of Rusty Bardiche",
        "advanced_format": "Unlimited",
        "traditional_format": "Unlimited",
        "remarks": "Was Limited"
    },
    { "card_type": "Monster/Synchro",
        "card_name": "Dewloren, Tiger King of the Ice Barrier",
        "advanced_format": "Unlimited",
        "traditional_format": "Unlimited",
        "remarks": "Was Limited"
    },
    {
        "card_type": "Monster/Synchro",
        "card_name": "Ignister Prominence, the Blasting Dracoslayer",
        "advanced_format": "Unlimited",
        "traditional_format": "Unlimited",
        "remarks": "Was Limited"
    },
    {
        "card_type": "Spell",
        "card_name": "Rank-Up-Magic Argent Chaos Force",
        "advanced_format": "Unlimited",
        "traditional_format": "Unlimited",
        "remarks": "Was Forbidden"
    },
    {
        "card_type": "Trap",
        "card_name": "True King\u2019s Return",
        "advanced_format": "Unlimited",
        "traditional_format": "Unlimited",
        "remarks": "Was Semi-Limited"
    }
]
```

## Licensing

Copyright (C) 2021 Dusan Mitrovic <dusan@dusanmitrovic.xyz>

This program is available under the terms of the GNU GPL. Either version 3 of the license or, at your option, any later version.
