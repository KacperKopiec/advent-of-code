let filename = "day11/input.in"

type graph = {
  edges: (string, string list) Hashtbl.t
} 

let parse s =
  let lst = String.split_on_char ' ' s in
  let hd = List.hd lst in
  let len = String.length hd in
  (String.sub hd 0 (len - 1), List.tl lst)

let g = 
  let edges = Advent.read_lines filename 
  |> List.map parse
  |> List.to_seq 
  |> Hashtbl.of_seq in {edges}

let order =
  let vis = Hashtbl.create 1024 in
  let lst = ref [] in
  let rec dfs v =
    Hashtbl.replace vis v true;
    let edges = Hashtbl.find_opt g.edges v |> Option.value ~default:[] in
    List.iter (fun e -> if not (Hashtbl.mem vis e) then dfs e else ()) edges;
    lst := v :: !lst
  in
  dfs "you";
  !lst

let dp = Hashtbl.create 1024

let solve = 
  let update node v =
    let prv_v = Hashtbl.find_opt dp node |> Option.value ~default:0 in
    Hashtbl.replace dp node (prv_v + v)
  in
  let rec aux = function
  | [] -> ()
  | x :: xs ->
    let v = Hashtbl.find_opt dp x |> Option.value ~default:0 in
    let edges = Hashtbl.find_opt g.edges x |> Option.value ~default:[] in
    List.iter (fun e -> update e v) edges;
    aux xs
  in
  Hashtbl.replace dp "you" 1;
  aux order;
  Hashtbl.find_opt dp "out" |> Option.value ~default:0

let () =
  solve
  |> Printf.printf "%d\n"
