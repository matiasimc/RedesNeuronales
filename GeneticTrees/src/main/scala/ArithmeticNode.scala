import scala.util.Random
package Arithmetic {

  trait ArithmeticNode {

    def evaluate(): Int = this match {
      case Number(n) => n
      case Plus(n1, n2) => n1.evaluate() + n2.evaluate()
      case Minus(n1, n2) => n1.evaluate() - n2.evaluate()
      case Mult(n1, n2) => n1.evaluate() * n2.evaluate()
      // se establece que x / 0 es x
      case Div(n1, n2) =>
        if (n2.evaluate() == 0) n1.evaluate()
        else n1.evaluate() / n2.evaluate()
    }

    /*
  Ejemplo: el arbol Minus(Plus(Number(2), Number(3)), Number(5))
  imprime
  ( - )
    ( + )
        ( 2 )
        ( 3 )
    ( 5 )
   */
    def prettyPrint(ident: Int = 0): Unit = this match {
      case Plus(n1, n2) =>
        print(" " * ident)
        println("( + )")
        n1.prettyPrint(ident + 4)
        n2.prettyPrint(ident + 4)

      case Minus(n1, n2) =>
        print(" " * ident)
        println("( - )")
        n1.prettyPrint(ident + 4)
        n2.prettyPrint(ident + 4)

      case Mult(n1, n2) =>
        print(" " * ident)
        println("( * )")
        n1.prettyPrint(ident + 4)
        n2.prettyPrint(ident + 4)

      case Div(n1, n2) =>
        print(" " * ident)
        println("( / )")
        n1.prettyPrint(ident + 4)
        n2.prettyPrint(ident + 4)

      case Number(n) =>
        print(" " * ident)
        println(s"( $n )")
    }

    def randomNode: ArithmeticNode = {
      val h = this.height
      val r = Random.nextInt(h)
      this match {
        case Plus(n1, n2) =>
          if (r == 0) this
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) n1.randomNode
            else n2.randomNode
          }
        case Minus(n1, n2) =>
          if (r == 0) this
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) n1.randomNode
            else n2.randomNode
          }
        case Mult(n1, n2) =>
          if (r == 0) this
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) n1.randomNode
            else n2.randomNode
          }
        case Div(n1, n2) =>
          if (r == 0) this
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) n1.randomNode
            else n2.randomNode
          }
        case Number(n) => this
      }
    }

    def replaceRandomNodeWith(node: ArithmeticNode): ArithmeticNode = {
      val h = this.height
      val r = Random.nextInt(h)
      this match {
        case Number(n) =>
          if (r == 0) node
          else this
        case Plus(n1, n2) =>
          if (r == 0) node
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) Plus(n1.replaceRandomNodeWith(node), n2)
            else Plus(n1, n2.replaceRandomNodeWith(node))
          }
        case Minus(n1, n2) =>
          if (r == 0) node
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) Minus(n1.replaceRandomNodeWith(node), n2)
            else Minus(n1, n2.replaceRandomNodeWith(node))
          }
        case Mult(n1, n2) =>
          if (r == 0) node
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) Mult(n1.replaceRandomNodeWith(node), n2)
            else Mult(n1, n2.replaceRandomNodeWith(node))
          }
        case Div(n1, n2) =>
          if (r == 0) node
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) Div(n1.replaceRandomNodeWith(node), n2)
            else Div(n1, n2.replaceRandomNodeWith(node))
          }
      }
    }

    def height: Int = this match {
      case Number(n) => 0
      case Plus(n1, n2) =>
        val lh = n1.height
        val rh = n2.height
        if (lh > rh) lh + 1
        else rh + 1
      case Minus(n1, n2) =>
        val lh = n1.height
        val rh = n2.height
        if (lh > rh) lh + 1
        else rh + 1
      case Mult(n1, n2) =>
        val lh = n1.height
        val rh = n2.height
        if (lh > rh) lh + 1
        else rh + 1
      case Div(n1, n2) =>
        val lh = n1.height
        val rh = n2.height
        if (lh > rh) lh + 1
        else rh + 1
    }

  }

  case class Number(n: Int) extends ArithmeticNode

  case class Plus(l: ArithmeticNode, r: ArithmeticNode) extends ArithmeticNode

  case class Minus(l: ArithmeticNode, r: ArithmeticNode) extends ArithmeticNode

  case class Mult(l: ArithmeticNode, r: ArithmeticNode) extends ArithmeticNode

  case class Div(l: ArithmeticNode, r: ArithmeticNode) extends ArithmeticNode

  object RandomArithmeticTree {
    /*
  Genera un arbol con cierta profundidad.
   */
    def generate(depth: Int): ArithmeticNode = {
      if (depth == 0) Number(Random.nextInt(100))
      else {
        Random.nextInt(4) match {
          case 0 => Plus(generate(depth - 1), generate(depth - 1))
          case 1 => Minus(generate(depth - 1), generate(depth - 1))
          case 2 => Mult(generate(depth - 1), generate(depth - 1))
          case _ => Div(generate(depth - 1), generate(depth - 1))
          //case _ => Number(new Random().nextInt(100))
        }
      }

    }
  }

}