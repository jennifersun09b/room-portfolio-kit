# Home music & podcast studio: real-world references

Room: `templates/music_studio.py` (themes: evening, daylight)

The room should read as a real spare-room studio that a musician or podcaster has put together from
well-known gear and IKEA furniture: a producer desk with rack bays, a pair of nearfield monitors on
isolation pads, a digital piano on an X-stand, a large-diaphragm condenser on a boom stand, an acoustic
guitar, a small tube combo and a KALLAX full of records with a direct-drive turntable on top.
Product and brand names appear only here and in code comments; the scene has no logos or brand text.

| Piece (slot) | Real reference | Real dimensions used | Recognisable details we model | Source |
|---|---|---|---|---|
| Desk (`desk`) | Producer desk in the style of the Output Platform / Studio RTA Producer Station | Top 152 x 70 x 2.5 cm at 74 cm; a 4U rack bay at each end of an 18 cm monitor bridge; an 8U 19-inch rack bay under the right side (Producer Station style); keyboard tray 67 x 30 cm | Wood-veneer slab sides and top, a modesty panel, a raised bridge across the back, 19-inch rack rails with screws, rack gear of different heights (1U = 4.45 cm), a pull-out tray with a computer keyboard | https://djmag.com/tech/output-launch-new-hardware-product , https://www.thomann.de/ie/studiorta_producer_station_cherry.htm , https://vintageking.com/recording/studio-furniture/de-fi-platform-studio-desk-natural |
| Nearfield monitors (on desk) | Yamaha HS5-type 5-inch two-way monitors | 17 x 22.2 x 28.5 cm (W x D x H) each | Sharp-edged black (or white) box, a white 5-inch woofer cone with a black surround and trim ring, a 1-inch dome tweeter in a shallow waveguide above it, a small power LED, toed in towards the chair | https://ca.yamaha.com/en/products/contents/proaudio/musicianspa/products_studio_monitor.html , https://www.andertons.co.uk/yamaha-hs5-powered-monitor-each-hs5 |
| Isolation pads (under monitors) | IsoAcoustics ISO-155 type | 15.5 x 19 cm footprint, 7.6 cm tall | Two plates joined by four posts with grey rubber isolators | https://zzounds.com/item--ISOISO155 |
| Audio interface (on desk) | Focusrite Scarlett 2i2 (4th gen) type | 18 x 9.9 x 4.55 cm | Red anodised body, two combo XLR inputs, two gain knobs with green halo rings, a big monitor knob, headphone jack | https://www.thomann.co.uk/focusrite_scarlett_2i2_4th_generation.htm |
| Mini MIDI controller (on desk) | Akai MPK Mini type 25-key controller | 31.8 x 18.1 x 4.4 cm | 25 mini keys, 2 x 4 drum pads, 8 knobs, a joystick | (standard mini-controller size) |
| Computer monitor (screen hook) | 27-inch office monitor on a rectangular stand | Panel 59.8 x 33.6 cm, 7 mm bezel, 2 cm chin | Thin bezel, chin, rectangular foot and flat neck | (standard 27-inch 16:9 size) |
| Office chair (`chair`) | IKEA MARKUS office chair | 62 x 60 cm, seat height 47 cm, back 129 cm | One-piece tall back that curves around you and narrows into the built-in headrest, on a black plastic shell and spine; fabric cover, five-star base with twin-wheel casters, gas lift with shroud, tilt mechanism, loop armrests | https://www.ikea.com/fi/en/p/markus-office-chair-vissle-light-grey-10521858 |
| Keyboard (`instrument`) | Yamaha P-45 type 88-key digital piano | 132.6 x 29.5 x 15.4 cm | 52 white and 36 black keys in the right 2-3 pattern starting on A, a red felt strip behind the keys, cheek blocks, a few buttons on the left, a music rest with sheet music, a square sustain pedal | https://usa.yamaha.com/products/musical_instruments/pianos/p_series/p-45/specs.html |
| Keyboard stand | On-Stage KS7191 double-braced X stand | Height 69-99 cm (set to 71 cm), arms 34 cm | Two parallel X frames, a central pivot with a big T-knob, rubber end caps on the feet, rubber pads on the arms | https://www.zzounds.com/item--MUPKS7191 |
| Condenser mic (`hero_prop`) | Rode NT1 (5th gen) type large-diaphragm condenser | Body 18.9 cm long, 5.2 cm diameter | Silver-finish cylinder body with a mesh head and rings (the 5th gen comes in black or silver; silver reads against a dark wall), an elastic shock mount with two rings, a 6-inch double-mesh pop filter on a gooseneck | https://edge.rode.com//pdf/products/1183/NT1%205th%20GEN_Datasheet.pdf |
| Boom stand (`hero_prop`) | K&M 210/9 type tripod boom stand (boom reach comparable to the PSA1's 82 cm) | Tube 93-160 cm, boom 80 cm | Folding tripod with a strut collar, clutch, boom with counterweight tipped 10 degrees down so the mic sits at the mouth height of someone on the sofa (about 1.15 m), XLR cable down the stand | https://edge.rode.com//pdf/products/1212/PSA1%20Black%20White_Data%20Sheet_FA.pdf |
| Headphones (on desk hook) | Audio-Technica ATH-M50x type closed-back headphones | Earcup about 8.5 x 10 x 4.6 cm | Padded headband, yokes, oval cups with leatherette pads, hung on a desk-side hook | https://www.crutchfield.com/S-Al0KmaQ2TXK/p_901M50X/Audio-Technica-ATH-M50x.html |
| Acoustic guitar (decor) | Yamaha F310 type dreadnought | Length 102.9 cm, body 50.5 x 41.2 cm, depth 9.6-11.6 cm, scale 63.4 cm | Dreadnought outline with square shoulders, spruce top, dark sides, cream binding, rosette, tortoiseshell pickguard, bridge with pins, 14 frets to the body, 3+3 headstock | https://usa.yamaha.com/products/musical_instruments/guitars_basses/ac_guitars/f_fx/specs.html |
| Guitar stand | Hercules GS414B type tripod stand | Height 95 cm, base radius 31 cm | Tripod legs, a padded lower cradle, a yoke that holds the neck | https://herculesstands.com/products/fretted-and-bowed-instrument/guitar/single-stands/gs414b-plus |
| Combo amp (`speaker`) | Fender Blues Junior (lacquered tweed) type 1x12 combo | 45.7 x 23.3 x 40.6 cm | Lacquered tweed covering with its diagonal twill stripe, brown striped grille cloth, chrome control panel on the top with chicken-head knobs, red jewel light, strap handle | https://www.thomann.co.uk/fender_blues_junior_tweed.htm |
| Record shelf (`shelf`) | IKEA KALLAX 77x77 shelving unit | 77 x 39 x 77 cm; 4 cm outer frame, 1.6 cm dividers, 33.5 cm cubes | The thick frame versus thin dividers, LPs (31.4 cm sleeves) standing in the cubes, a fabric box in one cube | https://www.ikea.com/qa/en/p/kallax-shelving-unit-white-20275814/ |
| Turntable (on KALLAX) | Technics SL-1200MK7 type direct-drive turntable | 45.3 x 35.3 x 16.9 cm | Platter with strobe dots, rubber mat, S-shaped tonearm with counterweight and arm rest, pitch fader, start/stop button, big round feet | https://technics.com/ca/products/dj-series/sl-1200mk7.html |
| Sofa (`sofa`) | IKEA LANDSKRONA 2-seat sofa, golden-brown leather | 164 x 89 x 78 cm, seat height 44 cm, arm 64 cm | Thin track arms, two seat cushions and two back cushions with piping, tapered wooden legs | https://www.ikea.com/au/en/files/pdf/49/d5/49d53ff6/landskrona_fy22_oct21.pdf |
| Floor lamp (`floor_lamp`) | IKEA HEKTAR floor lamp | 181 cm, shade 31.5 cm, base 34 cm | Heavy round base, thin stem, big dark-grey cone shade on a tilting joint | https://www.ikea.com/gb/en/p/hektar-floor-lamp-dark-grey-60216549/ |
| Wood slat panels (wall) | Woodupp Akupanel 240 type acoustic slat panels | 240 x 60 x 2.2 cm; slats 27 x 13 mm with 13 mm gaps on 9 mm black felt | Vertical veneer slats with black felt showing in the gaps | https://woodupp.co.uk/product/akupanel-240 |
| Acoustic foam (wall) | Auralex Studiofoam Wedgies type tiles (1 ft x 1 ft x 2 in) | 30 x 30 x 5 cm tiles, 2 x 3 grid | Triangular wedge ridges, tiles laid with the ridges alternating vertical / horizontal like a checkerboard | https://www.adorama.com/aurwedgie24.html |
| Record ledges (frame hooks) | IKEA MOSSLANDA picture ledge 115 cm | 115 x 12 cm | Shelf with a front lip and groove, LP sleeves (31.4 cm) leaning on it | https://www.ikea.com/no/en/p/mosslanda-picture-ledge-white-40291766/ |
| Rug (`rug`) | Vintage Persian-style wool rug | 200 x 140 cm | Navy border with guard stripes and a repeat motif, rust field covered in a small all-over flower repeat, a serrated (knotted-edge) diamond medallion with a pendant at each end, corner spandrels, fringes | (typical 4x6 ft Persian rug) |
| Name sign (name/role hooks) | Custom LED neon sign on black acrylic | 120 x 46 cm | Glowing tube letters on a glossy backboard held off the wall by chrome standoffs, power lead | (common custom neon sign format) |
| ON AIR light (wall) | Studio "ON AIR" LED warning light box | 34 x 11 x 7 cm | Black housing with a glowing red front and white letters | (generic studio warning light) |
| Posters (poster hooks) | IKEA RIBBA frames 50x70 and 30x40 | Outer 52 x 72 cm and 32 x 42 cm, 4.5 cm deep | Thin deep frame around a gig poster | https://www.ikea.com/my/en/p/ribba-frame-white-00378460 |
| Cajon (decor) | Box cajon (Meinl / Schlagwerk type) | 30 x 30 x 48 cm | Birch body, darker front plate with corner screws, rubber feet | (standard cajon size) |
| Plant (decor) | Snake plant (Sansevieria) in a glazed pot | Pot 22 cm, plant about 65 cm | Upright sword leaves with banding, pot rim and soil | (standard nursery size) |
| Radiator (decor) | Type 22 steel panel radiator under the window | 80 x 50 x 10 cm | Pressed vertical ribs, top grille, valve and pipes | https://www.wickes.co.uk/Type-22-Double-Panel-Compact-Radiator---White-600-x-1000mm/p/176238 |
| Floor | Engineered oak planks | 19 cm boards, 1.2-2.0 m long | Staggered end joints, slight tone change between boards, grain along the boards | (standard engineered oak board size) |

## Room language

A real home studio is a converted spare bedroom, not a sci-fi pod. The producer desk sits against the back
wall with its monitors forming a triangle with the chair, wood slat panels behind it (they look good and
tame reflections), and a strip of coloured LED light washing the wall. Rack gear is a mix of heights and
finishes: a silver two-unit preamp with VU meters, a black compressor, a power conditioner with an amber
read-out, blank and vented panels. The middle of the room is kept for playing: a digital piano on an
X-stand with a sustain pedal, a condenser on a tripod boom with a pop filter, a cajon, and a Persian-style
rug that every studio seems to own. The listening corner is a golden-brown leather two-seater beside the
window, an IKEA KALLAX full of records with a direct-drive turntable on top, LP sleeves leaning on picture
ledges and a neon name sign. Materials are honest: walnut and oak veneer, black felt, powder-coated steel,
brushed aluminium, lacquered tweed, leather, glazed ceramic, painted plaster walls with a skirting board and
oak floorboards.
