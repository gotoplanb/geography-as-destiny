---
id: fig-016
title: "The Shannon-Weaver Communication Model"
type: diagram
implementation: python
status: rendered
chapter: appendix-c
---

## What It Shows
The canonical block-diagram of the Shannon-Weaver communication model: an information source produces a message, the transmitter encodes it as a signal, the signal moves through a channel that is subject to noise, the receiver decodes the received signal back into a message, and the destination consumes it.

## Why It Matters
This is the picture behind the framework's epistemological apparatus. Historical sources are not transparent windows onto the past — they are messages produced by exactly this process. Official chronicles encode events for the senders' purposes. Channels (court archives, printing, oral tradition) introduce noise. Receivers (later historians, including the reader) reconstruct an approximation of the original. The framework's "Shannon-mode" reading treats every historical source as an artifact of this pipeline rather than as direct evidence of the events it nominally describes.

## Data Sources
- Shannon, Claude E. "A Mathematical Theory of Communication." *Bell System Technical Journal* 27 (July and October 1948): 379–423, 623–656.
- Shannon, Claude E., and Warren Weaver. *The Mathematical Theory of Communication*. Urbana: University of Illinois Press, 1949. (The block diagram in its classic published form appears in the Weaver-co-authored 1949 edition.)
- The diagram in this figure is the canonical block-diagram as it has appeared in communication-theory textbooks since 1949; it is a schematic reproduction, not a copy of any specific copyrighted rendering.

## Implementation Notes
- Python: matplotlib with fancy-bbox patches for rounded boxes
- Five primary boxes left-to-right: Information Source, Transmitter, Channel, Receiver, Destination
- Noise Source box below Channel with arrow up into Channel (rendered in red to mark it as the entropic element)
- Arrow labels: message (source→transmitter), signal (transmitter→channel), received signal (channel→receiver), message (receiver→destination)
- Title plus subtitle plus a bottom caption tying the diagram to the framework's use of it

## Sketch
```
[Information Source] → message → [Transmitter] → signal → [Channel] → received signal → [Receiver] → message → [Destination]
                                                              ↑
                                                       [Noise Source]
```
