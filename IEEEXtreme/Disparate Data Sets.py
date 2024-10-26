import csv
from dataclasses import dataclass
from typing import List, Dict, Set
from collections import defaultdict
import sys

@dataclass
class Event:
    event_id: str
    title: str
    acronym: str
    project_code: str
    three_digit_code: str
    record_type: str
    parent_id: str = ""

class EventProcessor:
    def __init__(self):
        self.events: Dict[str, Event] = {}
        self.parent_to_children: Dict[str, List[Event]] = defaultdict(list)
        self.acronym_to_parents: Dict[str, Set[str]] = defaultdict(set)
        
    def parse_record(self, record: str) -> Event:
 
        reader = csv.reader([record])
        event_id, title, acronym, project_code, three_digit_code, record_type = next(reader)
        return Event(event_id, title, acronym, project_code, three_digit_code, record_type)

    def process_events(self, lines: List[str]) -> List[str]:
    
        for line in lines:
            line = line.strip()
            if not line: 
                continue
            event = self.parse_record(line)
            self.events[event.event_id] = event
            
            if event.record_type == "Parent Event":
                if event.acronym:  
                    self.acronym_to_parents[event.acronym].add(event.event_id)
            else:  
                if event.acronym: 
                  
                    for parent_id in self.acronym_to_parents[event.acronym]:
                        self.parent_to_children[parent_id].append(event)
                        event.parent_id = parent_id

      
        valid_sets = []
        
     
        for parent_id, children in self.parent_to_children.items():
            parent = self.events[parent_id]
            
            
            if not children or not parent.acronym:
                continue
         
            child_codes = {child.three_digit_code for child in children}
            if len(child_codes) == 1:
                parent.three_digit_code = next(iter(child_codes))
            else:
                parent.three_digit_code = "???"
          
            if len(self.acronym_to_parents[parent.acronym]) == 1:
              
                set_output = []
                
               
                parent_record = f'{parent.event_id},"{parent.title}","{parent.acronym}",,{parent.three_digit_code},"{parent.record_type}"'
                set_output.append(parent_record)
                
               
                sorted_children = sorted(children, key=lambda x: (x.title, x.event_id))
                
              
                for child in sorted_children:
                    child_record = f'{child.event_id},"{child.title}","{child.acronym}",{child.project_code},{child.three_digit_code},"{child.record_type}",{parent.event_id}'
                    set_output.append(child_record)
                
                valid_sets.append((parent.acronym, set_output))
        
   
        valid_sets.sort()
    
        return [line for _, set_output in valid_sets for line in set_output]

def main():

    lines = []
    try:
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
    except EOFError:
        pass

    processor = EventProcessor()
    output = processor.process_events(lines)
    
    # Print output
    for line in output:
        print(line)

if __name__ == "__main__":
    main()