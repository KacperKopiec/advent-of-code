let filename = "day9/input.in"

let parse = function
| [x; y] -> (int_of_string x, int_of_string y)
| _ -> failwith "Invalid input"

let points = 
  Advent.read_lines filename 
  |> List.map (fun s -> parse (String.split_on_char ',' s))
  
let cords = 
  -1 :: List.fold_left (fun acc (x, y) -> x :: y :: acc) [] points 
  |> List.sort_uniq (fun x y -> compare x y)
  |> Array.of_list

let get_index n =
  let rec aux l r =
    if l > r then failwith "No such element"
    else begin
      let mid = (l + r) / 2 in
      let x = cords.(mid) in
      if n = x then mid
      else if x < n then aux (mid + 1) r
      else aux l (mid - 1)
    end
  in
  aux 0 (Array.length cords - 1)
  
let points_compressed = List.map (fun (x, y) -> (get_index x, get_index y)) points
  
let srt (p1, p2) = if p1 < p2 then (p1, p2) else (p2, p1)

let parse_segments lst = 
  let first = List.hd lst in
  let rest = List.tl lst in
  let rec aux lst prv acc =
    match lst with
    | [] -> srt ((prv, first)) :: acc
    | p :: lst' -> aux lst' p (srt ((prv, p)) :: acc) 
  in
  aux rest first []

let grid = let mx = Array.length cords + 2 in Array.make_matrix mx mx (-1)
let () =
  let rec aux = function
  | [] -> ()
  | ((x1, y1), (x2, y2)) :: lst ->
    if x1 = x2 then begin
      for i = y1 to y2 do
        grid.(i).(x1) <- 1;
      done;
      aux lst
    end else begin
      for i = x1 to x2 do
        grid.(y1).(i) <- 1;
      done;
      aux lst
    end
  in
  aux (parse_segments points_compressed);

  let q = Queue.create () in
  Queue.push (0, 0) q;
  grid.(0).(0) <- 0;
  while not (Queue.is_empty q) do
    let y, x = Queue.pop q in
    Seq.iter (fun (ny, nx) ->
      if grid.(ny).(nx) = -1 then begin
        grid.(ny).(nx) <- 0;
        Queue.push (ny, nx) q
      end  
    ) (Advent.neighbours grid y x Advent.directions)
  done;

  let len = Array.length grid in
  for i = 0 to len - 1 do
    for j = 0 to len - 1 do
      if grid.(i).(j) = -1 then grid.(i).(j) <- 1 
    done
  done

let pref = let mx = Array.length cords + 1 in Array.make_matrix mx mx 0
let () = 
  let len = Array.length pref in
  for i = 1 to (len - 1) do
    pref.(0).(i) <- pref.(0).(i - 1) + grid.(i).(0);
    pref.(i).(0) <- pref.(i - 1).(0) + grid.(0).(i);
  done;

  for i = 1 to len - 1 do
    for j = 1 to len - 1 do
      pref.(i).(j) <- pref.(i - 1).(j) + pref.(i).(j - 1) - pref.(i - 1).(j - 1) + grid.(i).(j);
    done
  done

let check x1 y1 x2 y2 =
  let xx1 = min x1 x2 in
  let xx2 = max x1 x2 in
  let yy1 = min y1 y2 in
  let yy2 = max y1 y2 in
  let area = (yy2 - yy1 + 1) * (xx2 - xx1 + 1) in
  let cnt_greens = pref.(yy2).(xx2) - pref.(yy2).(xx1 - 1) - pref.(yy1 - 1).(xx2) + pref.(yy1 - 1).(xx1 - 1) in
  area = cnt_greens

let cartasian lst1 lst2 =
  List.concat (List.map (fun e -> List.map (fun e' -> (e, e')) lst2) lst1 )

let rec solve acc = function
| [] -> acc
| ((x1, y1), (x2, y2)) :: lst' ->
    if check x1 y1 x2 y2 then begin
      let area = (abs (cords.(x1) - cords.(x2)) + 1) * (abs(cords.(y1) - cords.(y2)) + 1) in
      solve (max acc area) lst'
    end else solve (acc) lst'

let () =
  cartasian points_compressed points_compressed
  |> solve 0
  |> Printf.printf "%d\n"