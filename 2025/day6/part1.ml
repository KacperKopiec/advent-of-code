let filename = "day6/input.in"

let lines = 
  Advent.read_lines filename 
  |> List.map (String.split_on_char ' ') 
  |> List.map (List.filter (fun x -> x <> ""))
  |> List.rev

let numbers = 
  List.tl lines 
  |> List.map (List.map int_of_string) 
  |> Advent.zip

let operations = List.hd lines

let rec solve nums ops acc =
  match nums, ops with
  | [], [] -> acc
  | x :: xs, y :: ys -> solve xs ys (acc + if y = "+" then List.fold_left ( + ) 0 x else List.fold_left ( * ) 1 x)
  | _ -> failwith "Invalid input"

let () = 
  solve numbers operations 0
  |> Printf.printf "%d\n"