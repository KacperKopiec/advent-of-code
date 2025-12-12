let filename = "day12/input.in"

let parse lst =
  let rec aux lst acc1 acc2 =
    match lst with
    | [] -> acc1 :: acc2
    | x :: xs ->
      if x = "" then aux xs [] (acc1 :: acc2)
      else aux xs (x :: acc1) acc2
  in
  aux lst [] []

let parse_region s =
  let lst = String.split_on_char ' ' s in
  let area = List.hd lst in
  let xy = String.sub area 0 (String.length area - 1) in
  let x_y = String.split_on_char 'x' xy in
  let parse_x_y lst =
    match lst with
    | [x; y] -> (int_of_string x) * (int_of_string y)
    | _ -> failwith "Invalid input"
  in
  let tl = List.tl lst |> List.map int_of_string in
  (parse_x_y x_y, tl)

let parse_present lst =
  List.fold_left (fun acc s -> acc + String.fold_left (fun acc c -> acc + if c = '#' then 1 else 0) 0 s) 0 lst

let input = Advent.read_lines filename |> parse
let regions = List.hd input |> List.map parse_region
let presents = List.tl input |> List.rev |> List.map parse_present |> Array.of_list

let check region = 
  let area = fst region in
  let cnts = snd region in
  let sum = List.mapi (fun i x -> x * presents.(i)) cnts |> List.fold_left ( + ) 0 in
  sum < area

let () =
  List.filter check regions
  |> List.length
  |> Printf.printf "%d\n"