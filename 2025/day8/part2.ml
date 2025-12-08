let filename = "day8/input.in"

type find_union = {
  parents : int array;
  size : int array
}

let init_dsu n = 
  let par = Array.init n (fun i -> i) in
  let sz = Array.make n 1 in
  { parents = par; size = sz }

let rec find ds element =
  if ds.parents.(element) = element then element
  else
    let root = find ds ds.parents.(element) in
    ds.parents.(element) <- root;
    root

let union ds element1 element2 =
  let root1 = find ds element1 in
  let root2 = find ds element2 in
  if root1 <> root2 then
    let size1 = ds.size.(root1) in
    let size2 = ds.size.(root2) in
    if size1 >= size2 then begin
      ds.size.(root1) <- size1 + size2;
      ds.parents.(root2) <- root1;
      true
    end else begin 
      ds.size.(root2) <- size2 + size1;
      ds.parents.(root1) <- root2;
      true
    end
  else false

type point = {
  x : int;
  y : int;
  z : int;
  index : int;
}

let dist p1 p2 =
  let xx = p1.x - p2.x in
  let yy = p1.y - p2.y in
  let zz = p1.z - p2.z in
  sqrt(float_of_int (xx * xx + yy * yy + zz * zz))

let parse idx = function
| [a; b; c] -> { x = int_of_string a; y = int_of_string b; z = int_of_string c; index = idx }
| _ -> failwith "Invalid input"

let points = Advent.read_lines filename |> List.mapi (fun idx s -> parse idx (String.split_on_char ',' s))

let distances =
  let rec aux p acc = function
  | [] -> acc
  | x :: xs -> aux p ((dist p x, p, x) :: acc) xs
in
let rec fold acc = function
| [] -> acc
| x :: xs -> fold (aux x acc xs) xs
in
fold [] points |> List.sort (fun (d1, _, _) (d2, _, _) -> Float.compare d1 d2)

let dsu = init_dsu (List.length points)

let rec mst lst acc = 
  match lst with
  | [] -> acc
  | (_, p1, p2) :: xs ->
    let acc = if union dsu p1.index p2.index then p1.x * p2.x else acc in
    mst xs acc

let () =
  mst distances 0
  |> Printf.printf "%d\n"