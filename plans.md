# Goals

## Main
- create a game which is independent of ecs library
- use created game to compare relative performance of populare ecs libraries

## Side
- explore options of ecs deaign pattern
- show advantage of ecs over component design pattern

# Chapters

1. Intro
- what is ecs
- ecs libraries (incl. list of libraries we will be measuring)
- why are we doing this
- abstract layer and why it is not trivial
- what are the goals
2. Game specification
- what properties we require from the game
- camera, language, os
- describe the game
3. Implementation analysis
- decisions when working on abstract layer
  - reprezentace systemu
    - entityprocesor
    - rozhrani ecs knihoven
      - entity
      - component
      - world
      - system
      - query
      - proto entityprocesor
    - function inlining
      - co to je
      - kdy je funkce inlinovana
      - proto entityprocesor
  - ecs factory
  - component tag
- decisions when working on game itself
  - ai
    - state machines
    - behavior trees
    - goap
    - proc behavior trees?
    - ai v systemech
    - co ma byt soucasti ai
  - ecs
    - condition checking systems
    - events
    - reaction systems
  - procedural terrain
    - on cpu
    - on gpu
    - pathfinding problems with gpu
4. Implementation
- code base
- abstraction layer
- game world
- game data
- ai?
- villages and villagers
- systems and components
5. Hypothesis
- cache
- little bit of arch type and sparse set
- libraries which want components as classes
- archtype > sparse set > other
6. Measurements analysis
- why benchmark.net
- aproaches to measerumet
  - game loop
  - one iteration
  - n iterations
  - should rendering be included?
  - iterations of each system
  - measuring why playing
- na co neberem ohled
  - paralelni queries
  - reaction systemy
  - jine vykonostni vylepseni
7. Results
- how are doing measurements
- results
- analysis of results
8. Conclusion
- goals
  - pripomenout je
  - jak a jestli jsme je splnili
- what could be done better
  - design kodu
  - bugy
  - hra zbytecne slozita
- mozna budouci vylepseni
  - hra by mohla byt zajimavejsi
  - mereni behem hrani
  - cas pro kazdy ststem zvladt
  - prepinani knihovny za behu