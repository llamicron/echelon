var app = new Vue({
  el: "#main",
  data: {
    matrices: [
      // [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
      // [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
      // [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    ],
    matrixInput: "",
    error: ""
  },

  methods: {
    addMatrix() {
      matrix = this.getMatrix();
    },

    getMatrix() {
      // example input:
      // 2x + 3y - 7z = 2
      // x + 4y - 2z = 1
      // 7x + 4y - 2z = 7
      eqs = this.matrixInput.split('\n'); // One equation per line
      eqs = eqs.filter(function (n) { return n != "" }); // Delete empty strings

      // Ensure there are 3 and only 3 equations
      if (eqs.length != 3) {
        this.error = "You need to provide 3 equations";
        return false;
      } else {
        this.error = '';
      }

      newEq = []

      for (let i = 0; i < eqs.length; i++) {
        const eq = eqs[i];
        els = eq.split(' ');
        for (let i = 0; i < els.length; i++) {
          const element = els[i];
          if (element == '+' || element == '-' || element == '=') {
            els.splice(i, 1);
          }

          els[i] = els[i].replace(/\D/g, '');
        }
        newEq.push(els);
      }

      this.matrices.push(newEq);
    }
  }
})


