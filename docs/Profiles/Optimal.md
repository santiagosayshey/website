## Overview
"Optimal" is a meticulously crafted profile, laser-focused on securing the crème de la crème of home video. Unlike traditional profiles like Transparent that lean heavily on release groups, "Optimal" pivots towards audio and video features, ensuring that the quality of the release is paramount. By doing so, it minimizes the frequency of remux grabs, a crucial factor given the substantial size of these files. This approach also addresses the challenge posed by trackers like PTP, which often release top-tier remuxes without naming the release group.

## Installation

- See this github link to import the nessecary custom formats and profile into your Radarr setup:
- https://github.com/santiagosayshey/Profilarr
	- When prompted to select a profile, choose Optimal
# Score Breakdown

| Resolution       | Source          | Codec     | Tracker | Audio     | HDR               | Edition          | Score | Upgrade Until |
|------------------|-----------------|-----------|---------|-----------|-------------------|-----------------|-------|---------|
| [[2160p]]            | [[Blu-Ray ]]        | [[BD Remux]]  |         | [[DTS-X]]     |                   |                 | 60    | 320     |
|                  |[[Movies Anywhere]]  |           |         | [[TrueHD]]    |                   |                 | 50    |        |
|                  |                 |           |         | [[DTS-HD MA]] |                   |                 |       |       |
|                  | [[Amazon Prime]]    |           |         |           |                   |                 | 40    |      |
|                  | [[Apple TV+]]       |           |         |           |                   |                 |       |     |
|                  | [[Disney+]]         |           |         | [[FLAC]]      | [[DV]]                |                 | 30    |    |
|                  | [[Netflix]]         |           |         |           |                   |                 |       |   |
|                  | [[HBOMax]]          |           |         |           |                   |                 |       |  |
|                  | [[Hulu]]            |           |         |           | [[HDR10+]]            |                 | 20    |  |
|                  | [[Peacock]]         |           |         |           |                   |                 |       |  |
|                  | [[Paramount+]]      |           |         |           |                   |                 |       |  |
|                  | [[Roku]]            |           |         |           |                   |                 |       |  |
|                  | [[iTunes]]          |           |         | [[Atmos]]     | [[HDR10]]             |                 | 10    |  |
|                  |                 |           |         | [[DD+]]       |                   | [[Special]] | 0     ||
|                  |                 |           |         | [[DTS]]       |                   |                 |       |  |
|                  |                 |           |         | [[DD]]        |                   |                 |       |  |
| [[SD]]             | [[WEBRIP]]          | [[Xvid]]      | [[UHDBits]] |           | [[DV Only]]|                 | -9999 |         |
| [[720p]]             | [[DVD]]             | [[x264]]      |         |           |                   |                 |       |         |
| [[1080p]]            |                 | [[x265]]      |         |           |                   |                 |       |         |
|                  |                 | [[DVD Remux]] |         |           |                   |                 |       |         |

# The Essence of Optimal

#### 1. **Indexer Priority**: 
   - Recognizing the limitations of parsing release notes, "Optimal" leverages indexer priority. Releases from HDB and BHD are always prioritized, given their consistent track record of hosting superior releases, notably from FRaMeSToR and 3L.

#### 2. **Audio/Video Supremacy**: 
   - The heart of "Optimal" lies in its unwavering commitment to audio and video quality. This ensures that even if a release group isn't specified, the profile can still discern and select the best available remux based on its intrinsic quality.

#### 3. **Special Consideration for WiLDCAT**: 
   - Releases from WiLDCAT are almost always prioritized due to their enhanced HDR and Audio tracks, setting them apart in the remux landscape.

#### 4. **Fallback Mechanism**: 
   - "Optimal" is not just about waiting for the perfect release. It provides a fallback to 2160p WEB VODs, ensuring that new movies are promptly grabbed. However, once the UHD Blu-ray is out, the profile will seamlessly upgrade to that superior version.

# The Optimal Alternative

For those who don't mind multiple upgrades of a remux, there's an alternative: **Optimal v2.1**. This variant incorporates release groups in tandem with audio/video features, ensuring a more comprehensive approach to prioritizing releases.
## Score Breakdown


| Resolution | Source  | Internal   | Audio     | Channels | HDR       | Edition    | Score | Upgrade |
|------------|---------|------------|-----------|----------|-----------|------------|-------|---------|
|            | h265 BR | FraMeSToR  |           |          |           |            | 100   | 500     |
|            |         | WiLDCAT    | DTS-X     |          |           |            | 95    |         |
|            |         | playBD     | TRUEHD    |          |           |            | 90    |         |
|            |         |            | DTS-HD MA |          |           |            | 85    |         |
|            |         | PmP        | FLAC      |          |           |            | 80    |         |
|            |         | EPSiLON    |           |          | DV+HDR10+ |            | 70    |         |
|            |         | FLiGHTS    |           |          |           |            | 65    |         |
|            |         | KRaLiMaRKo |           |          |           |            | 60    |         |
|            |         | TRiTON     | DD+       | 7.1      | DV+HDR10  | Extended   | 50    |         |
|            | AMZN    | NTb        |           |          |           |            | 40    |         |
|            | ATVP    | FLUX       |           |          |           |            |       |         |
|            | DSNP    |            | DTS       | 5.1      | HDR10+    |            | 30    |         |
|            | NF      |            |           |          |           |            |       |         |
|            | HMAX    |            |           |          |           |            |       |         |
|            | HULU    | TOMMY      | DD        | Stereo   |           | Criterion  | 20    |         |
|            | PCOK    | TEPES      |           |          |           |            |       |         |
|            | PMTP    | playWEB    |           |          |           |            |       |         |
|            | iT      | Scene      | Atmos     | Mono     | HDR       | IMAX (WEB) | 10    |         |
| 2160p      |         |            |           |          |           |            | 0     |         |
| SD         | h264    |            |           |          | DV        | Theatrical | -1000 |         |
| 1080p      | x264    |            |           |          |           |            |       |         |
| 720p       | x265    |

