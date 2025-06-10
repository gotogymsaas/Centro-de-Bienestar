const { i18n } = require('./next-i18next.config');

module.exports = {
  i18n,
  // Para development remoto (ajusta tu IP si cambia):
  allowedDevOrigins: ['http://192.168.20.110:3000'],
};
