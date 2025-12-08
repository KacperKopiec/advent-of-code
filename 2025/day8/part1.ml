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
    end else begin 
      ds.size.(root2) <- size2 + size1;
      ds.parents.(root1) <- root2
    end

type point = {
  x : int;
  y : int;
  z : int;
  index : int;
}

let dist2 p1 p2 =
  let xx = p1.x - p2.x in
  let yy = p1.y - p2.y in
  let zz = p1.z - p2.z in
  xx * xx + yy * yy + zz * zz

let parse idx = function
| [a; b; c] -> { x = int_of_string a; y = int_of_string b; z = int_of_string c; index = idx }
| _ -> failwith "Invalid input"

let points = Advent.read_lines filename |> List.mapi (fun idx s -> parse idx (String.split_on_char ',' s))

let distances =
  let rec aux p acc = function
  | [] -> acc
  | x :: xs -> aux p ((dist2 p x, p.index, x.index) :: acc) xs
in
let rec fold acc = function
| [] -> acc
| x :: xs -> fold (aux x acc xs) xs
in
fold [] points |> List.sort (fun (d1, _, _) (d2, _, _) -> compare d1 d2)

let dsu = init_dsu (List.length points)

let connect iter = 
  let rec aux iter lst = 
    if iter = 0 then ()
    else begin
      match lst with
      | [] -> ()
      | (_, idx1, idx2) :: xs -> (
        union dsu idx1 idx2;
        aux (iter - 1) xs
      )
    end
  in
  aux iter distances

let take n lst =
  let rec aux n lst acc =
    if n = 0 then acc
    else begin
      match lst with 
      | [] -> acc
      | x :: xs -> aux (n - 1) xs (x :: acc)
    end
  in
  aux n lst []

module IntSet = Set.Make(Int)

let () = connect 1000

let () = 
  let s = IntSet.of_list (List.fold_left (fun acc p -> find dsu p.index :: acc) [] points) in
  IntSet.fold (fun x acc -> dsu.size.(x) :: acc) s []
  |> List.sort (fun x y -> compare y x)
  |> take 3
  |> List.fold_left ( * ) 1
  |> Printf.printf "%d\n"