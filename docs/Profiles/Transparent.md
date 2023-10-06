---
title: Transparent
date: 2023-10-06
---

# Overview
A dynamic profile focused on delivering the best balance between Quality, File Size and Universality. Grounded in data, "Transparent" evolves continually to select the release most likely to attain a 'Golden Popcorn' status. Rather than being bound by isolated audio or video quality metrics, this profile places trust in the reputations and track records of release groups. By leveraging a unique metric, the [[Golden Popcorn Performance Index]] (GPPi), "Transparent" harnesses historical data to identify release groups known for their consistent output of top-tier quality at a specific resolution, effectively balancing between resolution, quality and universality. 

## Installation

Review the guide on [[Importing Profiles & Custom Formats]] to import the necessary custom formats and profiles inside your Radarr installation.

# Score Breakdown

## 1080p Only
This version of transparent prioritises 1080p encodes and allows SD remuxes and encodes as fallback. 720p, 2160p and x265 encodes are not allowed. Choose this version if you are not on PTP.

| Resolution | Source          | Codec     | Internal | Audio     | Extras    | Flags        | Score | Threshold |
|------------|-----------------|-----------|----------|-----------|-----------|--------------|-------|---------|
|            |                 |           | HD T1    |           |           | [[1080p GP]]     | 120   | 320     |
|            |                 |           | HD T2    |           |           |              | 110   |         |
|            |                 |           | HD T3    |           |           |              | 100   |         |
|            |                 |           | HD T4    |           |           |              | 90    |         |
|            |                 |           | HD T5    |           |           |              | 80    |         |
|            |                 |           | HD T6    |           |           | [[HDB Internal]] | 70    |         |
| [[1080p]]      | [[Movies Anywhere]] |           |          |           |           |              | 60    |         |
|            | [[Amazon Prime]]    |           |          |           |           |              | 50    |         |
|            | [[Apple TV+]]       |           |          |           |           |              |       |         |
|            | [[Disney+]]         | [[DVD Remux]] |          |           |           |              | 40    |         |
|            | [[Netflix]]         |           |          |           |           |              |       |         |
|            | [[HBOMax]]          |           |          |           |           |              |       |         |
|            | [[Hulu]]            |           | SD T1    |           |           | [[SD GP]]        | 30    |         |
|            | [[Peacock]]         |           | HD T7    |           |           |              |       |         |
|            | [[Paramount+]]      |           |          |           |           |              |       |         |
|            | [[Roku]]            |           |          |           |           |              |       |         |
|            | [[iTunes]]          |           | SD T2    |           |         |              | 20    |         |
|            | [[Blu-Ray]]         | [[x264]]      |          | [[Atmos]]     | [[IMAX]]      |              | 10    |         |
|            | [[WEBRIP]]          |           |          |           | [[SE]] |              |       |         |
| [[480p]]       | [[DVD]]             | [[Xvid]]      |          | [[FLAC]]      | [[Criterion]]          |              | 0     |         |
|        |                 |           |          | [[DD+]]       |           |              |       |         |
|            |                 |           |          | [[DTS]]       |           |              |       |         |
|            |                 |           |          | [[DD]]        |           |              |       |         |
| [[720p]]           |                 | [[x265]]      |          | [[TrueHD]]    | [[Features]]  |              | -9999 |         |
| [[2160p]]      |                 | [[BD Remux]]  |          | [[DTS-HD MA]] |           |              |       |         |
|            |                 | [[Disc]]      |          | [[DTS-X]]     |

## 720p Fallback
In addition to the previous fallbacks, this version allows grabbing 720p golden popcorns when no reputable 1080p encode of WEB VOD is available. In the case that a 1080p encode from a reputable group is available, it is still prioritised over the 720p golden popcorn.

| Resolution | Source          | Codec     | Internal | Audio     | Extras    | Flags        | Score | Threshold |
|------------|-----------------|-----------|----------|-----------|-----------|--------------|-------|---------|
|            |                 |           | HD T1    |           |           | [[HD GP]]        | 120   | 320     |
|            |                 |           | HD T2    |           |           |              | 110   |         |
|            |                 |           | HD T3    |           |           |              | 100   |         |
|            |                 |           | HD T4    |           |           |              | 90    |         |
|            |                 |           | HD T5    |           |           |              | 80    |         |
|            |                 |           | HD T6    |           |           | [[HDB Internal]] | 70    |         |
| [[1080p]]      | [[Movies Anywhere]] |           |          |           |           |              | 60    |         |
|            | [[Amazon Prime]]    |           |          |           |           |              | 50    |         |
|            | [[Apple TV+]]       |           |          |           |           |              |       |         |
|            | [[Disney+]]         | [[DVD Remux]] |          |           |           |              | 40    |         |
|            | [[Netflix]]         |           |          |           |           |              |       |         |
|            | [[HBOMax]]          |           |          |           |           |              |       |         |
|            | [[Hulu]]            |           | SD T1    |           |           | [[SD GP]]        | 30    |         |
|            | [[Peacock]]         |           | HD T7    |           |           |              |       |         |
|            | [[Paramount+]]      |           |          |           |           |              |       |         |
|            | [[Roku]]            |           |          |           |           |              |       |         |
|            | [[iTunes]]          |           | SD T2    |           | [[SE]]        |              | 20    |         |
|            | [[Blu-Ray]]         | [[x264]]      |          | [[Atmos]]     | [[IMAX]]      |              | 10    |         |
|            | [[WEBRIP]]          |           |          |           | [[Criterion]] |              |       |         |
| [[480p]]       | [[DVD]]             | [[Xvid]]      |          | [[FLAC]]      |           |              | 0     |         |
|            |                 |           |          | [[DD+]]       |           |              |       |         |
|            |                 |           |          | [[DTS]]       |           |              |       |         |
|            |                 |           |          | [[DD]]        |           |              |       |         |
| [[720p]]       |                 |           |          |           |           |              | -120  |         |
| [[2160p]]      |                 | [[x265]]      |          | [[TrueHD]]    | [[Features]]  |              | -9999 |         |
|            |                 | [[BD Remux]]  |          | [[DTS-HD MA]] |           |              |       |         |
|            |                 | [[Disc]]      |          | [[DTS-X]]     |

## Remux Fallback
Coming Soon!

# Examples


# Discussion
## The Nuances of Transparency

### 1. Application Scope
   - **Existing Movies**: Typically, there's a single grab. However, upgrades might occur if a more reputable group releases a 'Golden Popcorn' version later. For instance, in the case of an already available reputable Blu-ray release, this profile may bypass web releases and opt for the reputable Blu-ray rip directly.
   - **Unreleased Movies**: Here, the journey is more layered. With VODs being the first to hit the market, a movie might undergo several upgrades. Initially, versions with constraints, such as Korean iTunes leaks with hardcoded subtitles, might be grabbed. This is progressively upgraded as more polished VODs become available, culminating in grabbing the most transparent available VOD, which is usually "Movies Anywhere". When the Blu-ray is out, patience is key. Instead of snapping up the immediate releases (which might not be the best), the profile waits for a reputable group's encode. The cycle of upgrades continues until it hits the upgrade threshold of 320 points. This threshold can be fine tuned by the user to account for upgrade immutability.

### 2. Handling Varying Resolutions
   - In scenarios where a VOD or Blu-ray is unavailable in the desired resolution, the profile uses SD as a fallback. There's a clear hierarchy: DVD remuxes take precedence, followed by SD 'Golden Popcorns', and then other internal SD encodes and VODs.
   - In the scenario that there exists no 1080p Golden Popcorn, 720p Golden Popcorns are prioritised over 1080p web VODS, SD encodes and DVD remuxes. On first glance, this doesn't seem *transparent* but please note that some 720p golden popcorns are more than sufficient in providing a transparent picture quality (and they save significantly more space). Once again, we place the trust in the release group the decide what is the best quality / size ratio. 

### 3. The Role of Indexer Flags
   - Beyond relying on data, the profile also utilizes indexer flags, especially with platforms like PassThePopcorn and HDBits. These flags are instrumental in handling exceptions where a 'Golden Popcorn' exists but hasn't been accounted for or when a more reputable group has actually encoded the 'Golden Popcorn'. This mechanism ensures that genuinely transparent releases are not missed.

### 4. Quality Profiles and Their Significance
   - Quality isn't merely about the source. There can be instances where a 4K VOD is 'webripped' to 1080p, offering a superior source compared to a standard 1080p Blu-ray encode. To ensure the best grab, various profiles like WEBRIP, BLURAY, and WEBDL are nested under a 'transparent capable' grouping, ensuring no specific source is prioritized over another.

## Custom Formats

The links in each of the score breakdowns are provided for you to tinker with if you want to modify them to suit your needs! They are not needed if you want to simply import the profile as is.

## Internal Tiers

A breakdown of each of the internal tiers can be found here: [[Release Group Tiers]]

## Indexer Priority

## Quality Hierarchy
In a nutshell, quality profiles are prioritised as such:

| Quality |
|---------|
|1080p Golden Popcorn|
|1080p WEB|
|1080p Bluray|
|720p Golden Popcorn|
|DVD Remux|
|SD Golden Popcorn|
|SD WEB|
