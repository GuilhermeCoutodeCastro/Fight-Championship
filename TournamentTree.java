import java.util.*;

public class TournamentTree {

    static class Node {
        String player;    // para folhas: nome do participante; para internos: null ou não usado
        String winner;    // vencedor registrado para o nodo (após simulação)
        Node left, right, parent;
        int id;           // id sequencial (começa em 1)

        private static int counter = 0;

        // Construtor para folha
        Node(String player) {
            this.player = player;
            this.id = ++counter;
        }

        // Construtor para nó interno (recebe filhos)

        Node(Node left, Node right) {
            this.left = left;
            this.right = right;
            if (left != null) left.parent = this;
            if (right != null) right.parent = this;
            this.id = ++counter;
        }

        boolean isLeaf() {
            return left == null && right == null;
        }

        // reinicia o contador (usar antes de construir a árvore)

        static void resetCounter() {
            counter = 0;
        }

        public String toString() {
        if (isLeaf()) {
            return String.format("Folha #%d: %s", id, player);
        } else {
        // Se já houver vencedor, mostra só o nome; senão indica que ainda não foi definido

            return String.format("Partida #%d: %s", id, 
            (winner == null ? "(a definir)" : winner));
        }
    }
    }

    private Node root;
    private int leafCount = 0;

    /**
     * Constroi a árvore a partir da lista de participantes (completa para potência de 2 usando "BYE").
     */

    public void buildFromList(List<String> players) {
        if (players == null || players.isEmpty()) throw new IllegalArgumentException("Lista vazia");
        Node.resetCounter();
        List<Node> nodes = new ArrayList<>();
        for (String p : players) {
            nodes.add(new Node(p));
        }
        leafCount = nodes.size();
        while (nodes.size() > 1) {
            List<Node> next = new ArrayList<>();
            for (int i = 0; i < nodes.size(); i += 2) {
                Node left = nodes.get(i);
                Node right = (i + 1 < nodes.size()) ? nodes.get(i + 1) : new Node("BYE");
                next.add(new Node(left, right));
            }
            nodes = next;
        }
        root = nodes.get(0);
    }

    /**
     * Obtém as rodadas como listas de partidas (cada lista corresponde a uma rodada,
     * iniciando da base (oitavas/1ª rodada) até a final).
     */

    private List<List<Node>> getRounds() {
        List<List<Node>> rounds = new ArrayList<>();
        if (root == null) return rounds;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            List<Node> round = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                Node cur = q.poll();
                if (cur.left != null) q.add(cur.left);
                if (cur.right != null) q.add(cur.right);
                if (!cur.isLeaf()) round.add(cur);
            }
            if (!round.isEmpty()) rounds.add(round);
        }
        Collections.reverse(rounds); // queremos da base até o topo
        return rounds;
    }

    /**
     * Simula o torneio inteiro de forma automática e imprime rodada por rodada.
     * Retorna o nome do campeão.
     */

    public String simulateTournament(Random rand) {
        if (root == null) return null;
        // limpa quaisquer winners anteriores

        clearWinners(root);

        List<List<Node>> rounds = getRounds();
        for (int i = 0; i < rounds.size(); i++) {
            int roundNumber = i + 1;
            boolean isFinal = (i == rounds.size() - 1);
            System.out.println(isFinal ? ("--- Rodada " + roundNumber + " (Final) ---") : ("--- Rodada " + roundNumber + " ---"));
            for (Node match : rounds.get(i)) {
                // garantir que os vencedores das subárvores estejam definidos

                String leftWinner = subtreeWinner(match.left);
                String rightWinner = subtreeWinner(match.right);

                if ("BYE".equals(leftWinner)) match.winner = rightWinner;
                else if ("BYE".equals(rightWinner)) match.winner = leftWinner;
                else match.winner = rand.nextBoolean() ? leftWinner : rightWinner;

                System.out.println(leftWinner + " vs " + rightWinner + " -> Vencedor: " + match.winner);
            }
            System.out.println();
        }
        // campeão no root.winner
        return root.winner;
    }

    // limpa winners recursivamente (para permitir múltiplas simulações no mesmo objeto)

    private void clearWinners(Node n) {
        if (n == null) return;
        n.winner = null;
        clearWinners(n.left);
        clearWinners(n.right);
    }

    // retorna o vencedor conhecido da subárvore (se for folha retorna player)
    // assume que após simulação todos nós internos terão winner definidos.

    private String subtreeWinner(Node n) {
        if (n == null) return "BYE";
        if (n.isLeaf()) {
            n.winner = n.player; // assegurar
            return n.player;
        }
        if (n.winner != null) return n.winner;
        // fallback: tente determinar a partir dos filhos (caso ainda não tenha sido simulado)

        String l = subtreeWinner(n.left);
        String r = subtreeWinner(n.right);
        if ("BYE".equals(l)) return r;
        if ("BYE".equals(r)) return l;
        // sem random aqui — mas este ramo só acontece se chamada antes da simulação completa

        return l; 
    }

    // --------------- Percursos ---------------

    public String preOrder() {
        StringBuilder sb = new StringBuilder();
        preOrder(root, sb);
        return sb.toString();
    }

    private void preOrder(Node n, StringBuilder sb) {
        if (n == null) return;
        sb.append(n).append("\n");
        preOrder(n.left, sb);
        preOrder(n.right, sb);
    }

    public String postOrder() {
        StringBuilder sb = new StringBuilder();
        postOrder(root, sb);
        return sb.toString();
    }

    private void postOrder(Node n, StringBuilder sb) {
        if (n == null) return;
        postOrder(n.left, sb);
        postOrder(n.right, sb);
        sb.append(n).append("\n");
    }

    public String breadthOrder() {
        StringBuilder sb = new StringBuilder();
        if (root == null) return sb.toString();
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            Node cur = q.poll();
            sb.append(cur).append("\n");
            if (cur.left != null) q.add(cur.left);
            if (cur.right != null) q.add(cur.right);
        }
        return sb.toString();
    }

    // --------------- Consultas estruturais ---------------

    public int height() {
        return height(root);
    }

    private int height(Node n) {
        if (n == null) return -1; // vazio = -1; folha = 0
        if (n.isLeaf()) return 0;
        return 1 + Math.max(height(n.left), height(n.right));
    }

    public int getLeafCount() {
        return leafCount;
    }

    public int getInternalCount() {
        return countNodes(root) - leafCount;
    }

    private int countNodes(Node n) {
        if (n == null) return 0;
        return 1 + countNodes(n.left) + countNodes(n.right);
    }

    // --------------- Análise entre jogadores (LCA e Caminho) ---------------

    /**
     * Encontra o nodo folha que contém exatamente o nome do jogador (comparação exata).
     */
    private Node findLeafByName(Node n, String name) {
        if (n == null) return null;
        if (n.isLeaf()) return name.equals(n.player) ? n : null;
        Node l = findLeafByName(n.left, name);
        if (l != null) return l;
        return findLeafByName(n.right, name);
    }

    /**
     * Verifica se um jogador (nome) está contido na subárvore n.
     */
    private boolean containsPlayer(Node n, String name) {
        return findLeafByName(n, name) != null;
    }

    /**
     * Encontra o Lowest Common Ancestor (LCA) dos dois nós folha correspondentes aos jogadores.
     * Retorna null se algum jogador não for encontrado.
     */
    public Node findLCA(String a, String b) {
        Node na = findLeafByName(root, a);
        Node nb = findLeafByName(root, b);
        if (na == null || nb == null) return null;
        return lowestCommonAncestor(na, nb);
    }

    private Node lowestCommonAncestor(Node a, Node b) {
        Set<Node> ancestors = new HashSet<>();
        Node cur = a;
        while (cur != null) { ancestors.add(cur); cur = cur.parent; }
        cur = b;
        while (cur != null) {
            if (ancestors.contains(cur)) return cur;
            cur = cur.parent;
        }
        return null;
    }

    /**
     * Retorna o caminho de partidas (lista de nós-match) que o jogador precisa vencer até a final.
     * Se o jogador já foi eliminado na simulação, indica em qual partida caiu (o primeiro ancestor cujo winner != jogador).
     * Retorna lista vazia se jogador não for encontrado.
     */
    public List<Node> pathToFinal(String player) {
        Node leaf = findLeafByName(root, player);
        if (leaf == null) return Collections.emptyList();
        List<Node> path = new ArrayList<>();
        Node cur = leaf.parent;
        while (cur != null) {
            path.add(cur);
            // se já foi definido vencedor diferente -> caiu aqui
            if (cur.winner != null && !cur.winner.equals(player)) {
                break;
            }
            cur = cur.parent;
        }
        return path;
    }

    /**
     * Para uma partida (nodo interno) e um jogador que participa dela (em uma das subárvores),
     * determina o oponente nessa partida (nome do vencedor da outra subárvore naquele momento).
     */
    private String opponentInMatchForPlayer(Node match, String player) {
        if (match == null) return "(desconhecido)";
        if (containsPlayer(match.left, player)) {
            return subtreeWinner(match.right);
        } else if (containsPlayer(match.right, player)) {
            return subtreeWinner(match.left);
        } else {
            return "(não participa)";
        }
    }

    // --------------- Utilitários para main ---------------

    private static String readLineTrim(Scanner sc) {
        String s = sc.nextLine();
        if (s == null) return "";
        return s.trim();
    }

    // --------------- Programa principal ---------------

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        TournamentTree tree = new TournamentTree();

        System.out.print("Digite o número de participantes (8 a 32): ");
        int n;
        try {
            n = Integer.parseInt(readLineTrim(sc));
        } catch (Exception e) {
            System.out.println("Entrada inválida. Encerrando.");
            sc.close();
            return;
        }
        if (n < 8 || n > 32) {
            System.out.println("Número de participantes deve ser entre 8 e 32. Encerrando.");
            sc.close();
            return;
        }

        List<String> players = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            System.out.print("Nome do participante " + (i + 1) + ": ");
            String name = readLineTrim(sc);
            if (name.isEmpty()) {
                System.out.println("Nome não pode ser vazio. Digite novamente.");
                i--;
                continue;
            }
            players.add(name);
        }

        // Ajusta para potência de 2 com BYE
        int pow2 = 1;
        while (pow2 < players.size()) pow2 <<= 1;
        while (players.size() < pow2) players.add("BYE");

        tree.buildFromList(players);

        System.out.println();
        System.out.println("===== SIMULANDO TORNEIO =====");
        System.out.println();

        String champion = tree.simulateTournament(rand);

        System.out.println("===== CAMPEÃO: " + champion + " =====");
        System.out.println();

        // Consultas estruturais
        System.out.println("=== Consultas Estruturais ===");
        System.out.println("Altura da árvore: " + tree.height());
        System.out.println("Número de folhas (participantes): " + tree.getLeafCount());
        System.out.println("Número de nós internos (partidas): " + tree.getInternalCount());
        System.out.println();

        // Percursos
        System.out.println("=== Percursos (texto) ===");
        System.out.println("--- Pré-Ordem ---");
        System.out.print(tree.preOrder());
        System.out.println("--- Pós-Ordem ---");
        System.out.print(tree.postOrder());
        System.out.println("--- Largura ---");
        System.out.print(tree.breadthOrder());
        System.out.println();

        // Pergunta ao final se deseja consultar LCA e Caminho
        while (true) {
            System.out.print("Deseja consultar LCA e Caminho de jogadores? (s/n): ");
            String opt = readLineTrim(sc).toLowerCase();
            if (!opt.equals("s")) break;

            System.out.print("Deseja consultar (1) LCA ou (2) Caminho de um jogador? Digite 1 ou 2: ");
            String choice = readLineTrim(sc);
            if (choice.equals("1")) {
                System.out.print("Nome do jogador 1: ");
                String j1 = readLineTrim(sc);
                System.out.print("Nome do jogador 2: ");
                String j2 = readLineTrim(sc);
                Node lca = tree.findLCA(j1, j2);
                if (lca == null) {
                    System.out.println("Um dos jogadores não foi encontrado na árvore.");
                } else {
                    // mostrar a partida (id) e os dois vencedores das subárvores (ou nomes)
                    String left = tree.subtreeWinner(lca.left);
                    String right = tree.subtreeWinner(lca.right);
                    System.out.println("LCA encontrado: Partida #" + lca.id + " -> " + left + " vs " + right);
                }
            } else if (choice.equals("2")) {
                System.out.print("Nome do jogador: ");
                String j = readLineTrim(sc);
                List<Node> path = tree.pathToFinal(j);
                if (path.isEmpty()) {
                    System.out.println("Jogador não encontrado.");
                } else {
                    System.out.println("Caminho do jogador até a final (do primeiro confronto até a final):");
                    boolean eliminated = false;
                    for (int i = 0; i < path.size(); i++) {
                        Node match = path.get(i);
                        String opponent = tree.opponentInMatchForPlayer(match, j);
                        String status;
                        if (match.winner != null && !match.winner.equals(j)) {
                            status = "Perdeu aqui (vencedor: " + match.winner + ")";
                            eliminated = true;
                        } else {
                            status = "Avançou (vencedor: " + match.winner + ")";
                        }
                        System.out.println("Partida #" + match.id + ": vs " + opponent + " -> " + status);
                        if (eliminated) break;
                    }
                    if (!eliminated) {
                        System.out.println("O jogador chegou até (ou é) o campeão: " + tree.root.winner);
                    }
                }
            } else {
                System.out.println("Opção inválida.");
            }
            System.out.println();
        }

        System.out.println("Encerrando.");
        sc.close();
    }
}
