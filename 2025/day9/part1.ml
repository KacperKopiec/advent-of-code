let filename = "day9/input.in"

let parse = function
| [x; y] -> (int_of_string x, int_of_string y)
| _ -> failwith "Invalid input"

let points = 
  Advent.read_lines filename 
  |> List.map (fun s -> parse (String.split_on_char ',' s))
  
let cartasian lst1 lst2 =
  List.concat (List.map (fun e -> List.map (fun e' -> (e, e')) lst2) lst1 )

let rec solve acc = function
| [] -> acc
| ((x1, y1), (x2, y2)) :: lst' ->
   let area = (abs (x1 - x2) + 1) * (abs(y1 - y2) + 1) in solve (max acc area) lst'

let () =
  cartasian points points
  |> solve 0
  |> Printf.printf "%d\n"