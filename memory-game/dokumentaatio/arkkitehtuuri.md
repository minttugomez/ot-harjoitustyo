```mermaid
classDiagram
    MemoryGame -- Grid
    Grid -- "72" Cards
    Cards "2" <|-- "1" Picture
    MemoryGame -- "1...4" Players
    Players <|-- "0...36" Points
```