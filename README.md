# AI Sign Language Translation Glove

A real-time assistive technology system that translates American Sign Language (ASL) hand gestures into spoken words. A sensor-embedded glove captures finger-bend data via an Arduino microcontroller, which is processed on a host PC using a K-Nearest Neighbor (KNN) algorithm, and delivered as audible speech through a text-to-speech engine — with live feedback displayed on a 16x2 LCD dashboard.

---

## Overview

The system operates as a continuous hardware-software handshake loop:

1. **Sense** — Five flex sensors (one per finger) are read as analog voltage values by the Arduino.
2. **Transmit** — The Arduino serializes the five readings and streams them over USB Serial to the host PC.
3. **Match** — The Python host receives each data frame and calculates the Euclidean distance between the live sensor vector and every stored gesture template using a KNN classifier.
4. **Speak** — The closest matching gesture label is passed to `pyttsx3` for immediate text-to-speech audio output.
5. **Display** — The recognized gesture and confidence data are sent back over Serial and rendered on the 16x2 LCD, completing the feedback loop.
