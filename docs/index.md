---
title: Ahoy!
draft: false
date: 2023-09-17
tags: []
---

Welcome to Dictionarry! This project aims to simplify media automation via tailored custom formats & profiles via Radarr & Sonarr.

## Background

Navigating the world of media quality and formats can be overwhelming. Questions like "Is 4k better than 1080p?" or "What's the difference between x264 and x265?" are common among the broader community.

I started this project to strip away the technical hassle and focus on what's important - getting the media you want. The idea is to fully automate your \*arr setup, tailoring them to your preferences. I've put together a set of quality profiles and custom formats that are all about hitting specific requirements:

1. Quality - A measure of visual and audio fidelity
2. Compatibility - Ensures your media files work well with your devices and software
3. Immutability - Determines if a file might be replaced with a better version

## How It Works

The core of this project is the [Profile Selector](https://selectarr.pages.dev/), a tool designed to guide users in choosing the right quality profile for their needs. This project is constantly evolving, so existing profiles are subject to change and new profiles will pop up all the time. Not all profiles in the Profile Selector are available but are currently being worked on. For now, check out the 1080p x264 Encode and 4K remux profiles. For a full roadmap of the profiles being worked on, check out the [Master Profile List](Profiles/index.md).

Once you've found your desired profile, check out [Profilarr](./Wiki/Importing%20Profiles%20&%20Custom%20Formats.md) for mass importing custom formats and profiles. This is another project I've been working on designed to make importing / exporting easier. It can also be used to easily sync CF's and QP's across multiple instances of Radarr / Sonarr in a single command.

## What Else?

I've tried to streamline and abstract this process as much as possible, but for those of you who wish to iterate on my custom formats and profiles, I've provided the raw json for all the custom formats I've used. These can be imported into Radarr / Sonarr / Lidarr and adjusted to suit your needs.

Feel free to use Profilarr to export / import / share your own setups too!

# # TRaSH Guides

Some custom formats found here have been interated on from the trash guides. Credit for these goes entirely to trash, and can be found on their site [here](https://trash-guides.info/). It is not my intention to steal their work, but rather to build on it and make it more accessible to the average user through my quality profiles. Please check out their site for more information on their work.
