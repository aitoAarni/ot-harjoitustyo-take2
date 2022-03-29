```mermaid
sequenceDiagram
    main -->> Machine: Machine()
    Machine -->>+ FuelTank()
    Machine -->> FuelTank: fill(40)
    Machine->>+FuelTank: Hello John, how are you?
    Alice->>John: John, can you hear me?
    John-->>Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
        
    
```
