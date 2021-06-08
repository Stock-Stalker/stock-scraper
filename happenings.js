// Display 'Happenings' page
const Happenings = require('../models/happening')

exports.getHappenings = async (req, res) => {
  const currentPage = req.query.page || 1
  const perPage = 10
  const count = await Happenings.find().countDocuments()
  const happenings = await Happenings.find().lean().skip((currentPage - 1) * perPage).limit(perPage)
  res.render('happenings', {
    happenings: happenings,
    pagesCount: count / perPage,
    currentPage: currentPage
  })
}
