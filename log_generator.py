from typing import Generator

def stream_log_lines(filepath)->Generator[str,None, None]:
    with open(filepath ,"r", encoding="urf-8") as file:
        for lines in file:
            clean = lines.strip()
            if clean:
                yield clean
def chunk_generator(lines:list[str], chunk_size:int = 5 )-> Generator[str, None, None]:
    for i in range(0, len(lines), chunk_size):
         yield lines [i: i + chunk_size]
